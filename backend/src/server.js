const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const dotenv = require('dotenv');
const { Pool } = require('pg');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const { v4: uuidv4 } = require('uuid');

dotenv.config();

const app = express();
const pool = new Pool({
  host: process.env.DB_HOST || 'database',
  port: process.env.DB_PORT || 5432,
  database: process.env.DB_NAME || 'saas_db',
  user: process.env.DB_USER || 'postgres',
  password: process.env.DB_PASSWORD || 'postgres',
  max: 20,
  idleTimeoutMillis: 30000,
  connectionTimeoutMillis: 2000,
});

// Middleware
app.use(helmet());
app.use(cors({
  origin: process.env.FRONTEND_URL || 'http://localhost:3000',
  credentials: true,
}));
app.use(express.json());

// Health Check
app.get('/api/health', async (req, res) => {
  try {
    const result = await pool.query('SELECT NOW()');
    res.json({ status: 'ok', database: 'connected', timestamp: new Date() });
  } catch (error) {
    res.status(503).json({ status: 'error', database: 'disconnected', message: error.message });
  }
});

// JWT Verification Middleware
const verifyToken = (req, res, next) => {
  const token = req.headers.authorization?.split(' ')[1];
  if (!token) return res.status(401).json({ success: false, message: 'No token provided' });
  
  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET || 'your-secret-key');
    req.user = decoded;
    next();
  } catch (error) {
    res.status(401).json({ success: false, message: 'Invalid token' });
  }
};

// Authorization Middleware
const authorize = (roles) => (req, res, next) => {
  if (!roles.includes(req.user.role)) {
    return res.status(403).json({ success: false, message: 'Unauthorized access' });
  }
  next();
};

// Tenant Isolation Helper
const getTenantIdFromContext = (req) => {
  if (req.user.role === 'super_admin') return null;
  return req.user.tenantId;
};

// Audit Logger
const logAudit = async (tenantId, userId, action, entityType, entityId, ipAddress) => {
  try {
    await pool.query(
      `INSERT INTO audit_logs (tenant_id, user_id, action, entity_type, entity_id, ip_address)
       VALUES ($1, $2, $3, $4, $5, $6)`,
      [tenantId, userId, action, entityType, entityId, ipAddress]
    );
  } catch (error) {
    console.error('Audit log error:', error);
  }
};

// ==================== AUTHENTICATION ENDPOINTS ====================

// API 1: Register Tenant
app.post('/api/auth/register-tenant', async (req, res) => {
  const { tenantName, subdomain, adminEmail, adminPassword, adminFullName } = req.body;
  
  try {
    if (!tenantName || !subdomain || !adminEmail || !adminPassword || !adminFullName) {
      return res.status(400).json({ success: false, message: 'Missing required fields' });
    }
    
    if (adminPassword.length < 8) {
      return res.status(400).json({ success: false, message: 'Password must be at least 8 characters' });
    }

    const client = await pool.connect();
    try {
      await client.query('BEGIN');

      // Check subdomain uniqueness
      const subdomainCheck = await client.query('SELECT id FROM tenants WHERE subdomain = $1', [subdomain]);
      if (subdomainCheck.rows.length > 0) {
        await client.query('ROLLBACK');
        return res.status(409).json({ success: false, message: 'Subdomain already exists' });
      }

      // Create tenant
      const tenantId = uuidv4();
      const maxUsers = 5; // free plan
      const maxProjects = 3;
      
      await client.query(
        `INSERT INTO tenants (id, name, subdomain, status, subscription_plan, max_users, max_projects)
         VALUES ($1, $2, $3, $4, $5, $6, $7)`,
        [tenantId, tenantName, subdomain, 'active', 'free', maxUsers, maxProjects]
      );

      // Hash password
      const passwordHash = await bcrypt.hash(adminPassword, 10);

      // Create admin user
      const userId = uuidv4();
      await client.query(
        `INSERT INTO users (id, tenant_id, email, password_hash, full_name, role, is_active)
         VALUES ($1, $2, $3, $4, $5, $6, $7)`,
        [userId, tenantId, adminEmail, passwordHash, adminFullName, 'tenant_admin', true]
      );

      await client.query('COMMIT');
      
      res.status(201).json({
        success: true,
        message: 'Tenant registered successfully',
        data: {
          tenantId,
          subdomain,
          adminUser: {
            id: userId,
            email: adminEmail,
            fullName: adminFullName,
            role: 'tenant_admin'
          }
        }
      });
    } catch (error) {
      await client.query('ROLLBACK');
      throw error;
    } finally {
      client.release();
    }
  } catch (error) {
    res.status(500).json({ success: false, message: error.message });
  }
});

// API 2: Login
app.post('/api/auth/login', async (req, res) => {
  const { email, password, tenant
