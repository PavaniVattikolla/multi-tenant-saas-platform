const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const dotenv = require('dotenv');
const { v4: uuidv4 } = require('uuid');

dotenv.config();

const app = express();

// Middleware
app.use(helmet());
app.use(cors({ origin: '*', credentials: true }));
app.use(express.json());

// In-memory storage
const store = {
  tenants: {},
  users: {},
  projects: {},
  tasks: {},
};

// Health Check
app.get('/api/health', (req, res) => {
  res.json({ status: 'UP', message: 'Multi-tenant SaaS Backend is healthy' });
});

// Root Route
app.get('/', (req, res) => {
  res.send('Multi-Tenant SaaS Backend Running');
});

// ==================== AUTHENTICATION ====================
// Register Tenant
app.post('/api/auth/register-tenant', (req, res) => {
  const { tenantName, subdomain, adminEmail, adminPassword, adminFullName } = req.body;
  if (!tenantName || !subdomain || !adminEmail || !adminPassword) {
    return res.status(400).json({ success: false, message: 'Missing required fields' });
  }
  const tenantId = uuidv4();
  const userId = uuidv4();
  store.tenants[tenantId] = { id: tenantId, name: tenantName, subdomain, status: 'active' };
  store.users[userId] = { id: userId, tenantId, email: adminEmail, name: adminFullName, role: 'tenant_admin' };
  res.status(201).json({ success: true, data: { tenantId, subdomain, userId, email: adminEmail } });
});

// Login
app.post('/api/auth/login', (req, res) => {
  const { email, password } = req.body;
  const user = Object.values(store.users).find(u => u.email === email);
  if (!user) return res.status(401).json({ success: false, message: 'Invalid credentials' });
  res.json({ success: true, data: { userId: user.id, tenantId: user.tenantId, email: user.email, token: 'mock-token' } });
});

// Logout
app.post('/api/auth/logout', (req, res) => {
  res.json({ success: true, message: 'Logged out successfully' });
});

// Refresh Token
app.post('/api/auth/refresh', (req, res) => {
  res.json({ success: true, token: 'new-mock-token' });
});

// ==================== TENANT MANAGEMENT ====================
// Get All Tenants
app.get('/api/tenants', (req, res) => {
  res.json({ success: true, data: Object.values(store.tenants) });
});

// Create Tenant
app.post('/api/tenants', (req, res) => {
  const { name, subdomain } = req.body;
  const tenantId = uuidv4();
  store.tenants[tenantId] = { id: tenantId, name, subdomain, status: 'active' };
  res.status(201).json({ success: true, data: store.tenants[tenantId] });
});

// Get Tenant Details
app.get('/api/tenants/:tenantId', (req, res) => {
  const tenant = store.tenants[req.params.tenantId];
  if (!tenant) return res.status(404).json({ success: false, message: 'Tenant not found' });
  res.json({ success: true, data: tenant });
});

// Update Tenant
app.put('/api/tenants/:tenantId', (req, res) => {
  const tenant = store.tenants[req.params.tenantId];
  if (!tenant) return res.status(404).json({ success: false, message: 'Tenant not found' });
  Object.assign(tenant, req.body);
  res.json({ success: true, data: tenant });
});

// Delete Tenant
app.delete('/api/tenants/:tenantId', (req, res) => {
  delete store.tenants[req.params.tenantId];
  res.json({ success: true, message: 'Tenant deleted' });
});

// ==================== USER MANAGEMENT ====================
// Get All Users
app.get('/api/users', (req, res) => {
  res.json({ success: true, data: Object.values(store.users) });
});

// Create User
app.post('/api/users', (req, res) => {
  const { tenantId, email, password, name } = req.body;
  const userId = uuidv4();
  store.users[userId] = { id: userId, tenantId, email, name, role: 'user' };
  res.status(201).json({ success: true, data: store.users[userId] });
});

// Get User Details
app.get('/api/users/:userId', (req, res) => {
  const user = store.users[req.params.userId];
  if (!user) return res.status(404).json({ success: false, message: 'User not found' });
  res.json({ success: true, data: user });
});

// Update User
app.put('/api/users/:userId', (req, res) => {
  const user = store.users[req.params.userId];
  if (!user) return res.status(404).json({ success: false, message: 'User not found' });
  Object.assign(user, req.body);
  res.json({ success: true, data: user });
});

// Delete User
app.delete('/api/users/:userId', (req, res) => {
  delete store.users[req.params.userId];
  res.json({ success: true, message: 'User deleted' });
});

// ==================== PROJECT MANAGEMENT ====================
// Get All Projects
app.get('/api/projects', (req, res) => {
  res.json({ success: true, data: Object.values(store.projects) });
});

// Create Project
app.post('/api/projects', (req, res) => {
  const { tenantId, name, description } = req.body;
  const projectId = uuidv4();
  store.projects[projectId] = { id: projectId, tenantId, name, description, status: 'active', createdAt: new Date() };
  res.status(201).json({ success: true, data: store.projects[projectId] });
});

// Get Project Details
app.get('/api/projects/:projectId', (req, res) => {
  const project = store.projects[req.params.projectId];
  if (!project) return res.status(404).json({ success: false, message: 'Project not found' });
  res.json({ success: true, data: project });
});

// Update Project
app.put('/api/projects/:projectId', (req, res) => {
  const project = store.projects[req.params.projectId];
  if (!project) return res.status(404).json({ success: false, message: 'Project not found' });
  Object.assign(project, req.body);
  res.json({ success: true, data: project });
});

// Delete Project
app.delete('/api/projects/:projectId', (req, res) => {
  delete store.projects[req.params.projectId];
  res.json({ success: true, message: 'Project deleted' });
});

// ==================== TASK MANAGEMENT ====================
// Get All Tasks
app.get('/api/tasks', (req, res) => {
  res.json({ success: true, data: Object.values(store.tasks) });
});

// Create Task
app.post('/api/tasks', (req, res) => {
  const { projectId, title, description, assignedTo } = req.body;
  const taskId = uuidv4();
  store.tasks[taskId] = { id: taskId, projectId, title, description, assignedTo, status: 'pending', createdAt: new Date() };
  res.status(201).json({ success: true, data: store.tasks[taskId] });
});

// Get Task Details
app.get('/api/tasks/:taskId', (req, res) => {
  const task = store.tasks[req.params.taskId];
  if (!task) return res.status(404).json({ success: false, message: 'Task not found' });
  res.json({ success: true, data: task });
});

// Update Task
app.put('/api/tasks/:taskId', (req, res) => {
  const task = store.tasks[req.params.taskId];
  if (!task) return res.status(404).json({ success: false, message: 'Task not found' });
  Object.assign(task, req.body);
  res.json({ success: true, data: task });
});

// Delete Task
app.delete('/api/tasks/:taskId', (req, res) => {
  delete store.tasks[req.params.taskId];
  res.json({ success: true, message: 'Task deleted' });
});

// Start server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Multi-tenant SaaS Backend running on port ${PORT}`);
});
