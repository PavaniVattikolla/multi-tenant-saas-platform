# System Architecture

## Overview

This document describes the system architecture of the Multi-Tenant SaaS Platform, including the high-level design, component interactions, and deployment structure.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                         Frontend Layer                       │
│              React App (Port 3000)                          │
│   - Login/Register  - Dashboard  - Projects  - Tasks        │
└────────────────────────┬────────────────────────────────────┘
                         │ HTTP/REST API
                         │
┌────────────────────────┴────────────────────────────────────┐
│                      Backend Layer                           │
│              Node.js + Express (Port 5000)                  │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │     Auth     │  │    Tenant    │  │   Project    │     │
│  │  Controller  │  │  Controller  │  │  Controller  │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │     User     │  │     Task     │  │    Audit     │     │
│  │  Controller  │  │  Controller  │  │  Controller  │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │           Middleware Layer                           │   │
│  │  - Authentication  - Authorization  - Error Handler │   │
│  └─────────────────────────────────────────────────────┘   │
└────────────────────────┬────────────────────────────────────┘
                         │ SQL Queries
                         │
┌────────────────────────┴────────────────────────────────────┐
│                     Database Layer                           │
│              PostgreSQL (Port 5432)                         │
│                                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ tenants  │  │  users   │  │ projects │  │  tasks   │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
│                                                              │
│  ┌──────────────────────────────────────┐                  │
│  │         audit_logs                    │                  │
│  └──────────────────────────────────────┘                  │
└─────────────────────────────────────────────────────────────┘
```

## Component Description

### Frontend Layer
- **Technology**: React.js
- **Port**: 3000
- **Responsibilities**:
  - User interface rendering
  - Client-side routing
  - API consumption
  - State management
  - Form validation

### Backend Layer
- **Technology**: Node.js + Express.js
- **Port**: 5000
- **Responsibilities**:
  - RESTful API endpoints
  - Business logic processing
  - Authentication & authorization
  - Data validation
  - Database operations

### Database Layer
- **Technology**: PostgreSQL
- **Port**: 5432
- **Responsibilities**:
  - Data persistence
  - Data integrity
  - Transaction management
  - Query optimization

## Database Schema

### Tables

#### tenants
- id (UUID, Primary Key)
- name (VARCHAR)
- subdomain (VARCHAR, UNIQUE)
- status (ENUM: active, inactive, suspended)
- subscription_plan (VARCHAR)
- max_users (INTEGER)
- max_projects (INTEGER)
- created_at (TIMESTAMP)
- updated_at (TIMESTAMP)

#### users
- id (UUID, Primary Key)
- tenant_id (UUID, Foreign Key)
- email (VARCHAR, UNIQUE)
- password_hash (VARCHAR)
- full_name (VARCHAR)
- role (ENUM: super_admin, tenant_admin, user)
- status (ENUM: active, inactive)
- created_at (TIMESTAMP)
- updated_at (TIMESTAMP)

#### projects
- id (UUID, Primary Key)
- tenant_id (UUID, Foreign Key)
- name (VARCHAR)
- description (TEXT)
- status (ENUM: active, completed, archived)
- created_by (UUID, Foreign Key to users)
- created_at (TIMESTAMP)
- updated_at (TIMESTAMP)

#### tasks
- id (UUID, Primary Key)
- project_id (UUID, Foreign Key)
- tenant_id (UUID, Foreign Key)
- title (VARCHAR)
- description (TEXT)
- status (ENUM: todo, in_progress, completed)
- priority (ENUM: low, medium, high)
- assigned_to (UUID, Foreign Key to users)
- created_by (UUID, Foreign Key to users)
- due_date (DATE)
- created_at (TIMESTAMP)
- updated_at (TIMESTAMP)

#### audit_logs
- id (UUID, Primary Key)
- tenant_id (UUID, Foreign Key)
- user_id (UUID, Foreign Key)
- action (VARCHAR)
- resource_type (VARCHAR)
- resource_id (UUID)
- details (JSONB)
- ip_address (VARCHAR)
- created_at (TIMESTAMP)

## API Endpoints

### Authentication
1. **POST /api/auth/register-tenant** - Register new tenant
2. **POST /api/auth/login** - User login
3. **GET /api/auth/me** - Get current user
4. **POST /api/auth/logout** - User logout

### Tenants
5. **GET /api/tenants/:tenantId** - Get tenant details
6. **PUT /api/tenants/:tenantId** - Update tenant
7. **GET /api/tenants** - List all tenants (super admin only)

### Users
8. **POST /api/tenants/:tenantId/users** - Create user
9. **GET /api/tenants/:tenantId/users** - List tenant users
10. **PUT /api/users/:userId** - Update user

### Projects
11. **POST /api/tenants/:tenantId/projects** - Create project
12. **GET /api/tenants/:tenantId/projects** - List projects
13. **GET /api/projects/:projectId** - Get project details
14. **PUT /api/projects/:projectId** - Update project
15. **DELETE /api/projects/:projectId** - Delete project

### Tasks
16. **POST /api/projects/:projectId/tasks** - Create task
17. **GET /api/projects/:projectId/tasks** - List tasks
18. **PUT /api/tasks/:taskId** - Update task
19. **DELETE /api/tasks/:taskId** - Delete task

### Health Check
20. **GET /api/health** - Health check endpoint

## Security Architecture

### Authentication
- JWT-based token authentication
- Token expiry: 24 hours (configurable)
- Secure password hashing with bcrypt (10 rounds)

### Authorization
- Role-based access control (RBAC)
- Tenant isolation at database query level
- Middleware-based permission checking

### Data Isolation
- Every query filtered by tenant_id
- Row-level security
- Tenant context validation

## Docker Architecture

### Services

#### Database Service
- Image: postgres:15-alpine
- Container Name: multi-tenant-db
- Port Mapping: 5432:5432
- Volume: postgres_data

#### Backend Service
- Build: backend/Dockerfile
- Container Name: multi-tenant-backend
- Port Mapping: 5000:5000
- Depends On: database (with health check)

#### Frontend Service
- Build: frontend/Dockerfile
- Container Name: multi-tenant-frontend
- Port Mapping: 3000:3000
- Depends On: backend

### Network
- Network Name: saas-network
- Driver: bridge
- Enables inter-service communication

## Deployment Flow

1. **Docker Compose Up**
   ```bash
   docker-compose up -d
   ```

2. **Database Initialization**
   - PostgreSQL container starts
   - Health check validates database is ready
   - Migrations run automatically from `/docker-entrypoint-initdb.d`

3. **Backend Startup**
   - Waits for database health check
   - Runs migrations (if not already run)
   - Loads seed data automatically
   - Starts Express server on port 5000

4. **Frontend Startup**
   - Waits for backend to be ready
   - Serves React app on port 3000

## Scalability Considerations

- Horizontal scaling: Multiple backend instances behind load balancer
- Database: Connection pooling, read replicas
- Caching: Redis for session management
- CDN: Static asset delivery
- Monitoring: Health checks, logging, metrics

## Error Handling

- Centralized error middleware
- Structured error responses
- Logging with Winston
- Graceful degradation

## Monitoring & Logging

- Application logs
- Audit logs for all user actions
- Health check endpoints
- Database query logging (development mode)
