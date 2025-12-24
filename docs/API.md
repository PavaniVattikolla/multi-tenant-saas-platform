# API Documentation

## Base URL
- Local: `http://localhost:5000/api`
- Docker: `http://backend:5000/api`

## Health Check

### GET /api/health
Check system and database health status.

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "status": "ok",
    "database": "connected",
    "timestamp": "2025-12-24T09:00:00Z"
  }
}
```

---

## Authentication APIs

### POST /api/auth/register-tenant
Register a new tenant organization.

**Request Body:**
```json
{
  "tenantName": "My Company",
  "subdomain": "mycompany",
  "email": "admin@mycompany.com",
  "password": "SecurePassword@123",
  "fullName": "Admin Name"
}
```

**Response (201 Created):**
```json
{
  "success": true,
  "message": "Tenant registered successfully",
  "data": {
    "tenantId": "uuid",
    "tenant": {
      "id": "uuid",
      "name": "My Company",
      "subdomain": "mycompany",
      "subscriptionPlan": "free",
      "maxUsers": 5,
      "maxProjects": 3
    },
    "user": {
      "id": "uuid",
      "email": "admin@mycompany.com",
      "role": "tenant_admin"
    },
    "token": "eyJhbGc..."
  }
}
```

### POST /api/auth/login
Login with tenant credentials.

**Request Body:**
```json
{
  "email": "admin@demo.com",
  "password": "Demo@123",
  "tenantSubdomain": "demo"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Login successful",
  "data": {
    "token": "eyJhbGc...",
    "user": {
      "id": "uuid",
      "email": "admin@demo.com",
      "fullName": "Demo Admin",
      "role": "tenant_admin"
    },
    "tenant": {
      "id": "uuid",
      "name": "Demo Company",
      "subdomain": "demo"
    }
  }
}
```

### GET /api/auth/me
Get current user information.

**Headers:**
```
Authorization: Bearer {token}
```

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "id": "uuid",
    "email": "admin@demo.com",
    "fullName": "Demo Admin",
    "role": "tenant_admin",
    "tenant": {
      "id": "uuid",
      "name": "Demo Company"
    }
  }
}
```

### POST /api/auth/logout
Logout current user.

**Headers:**
```
Authorization: Bearer {token}
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Logged out successfully"
}
```

---

## Tenant Management APIs

### GET /api/tenants/:tenantId
Get tenant details and statistics.

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "id": "uuid",
    "name": "Demo Company",
    "subdomain": "demo",
    "status": "active",
    "subscriptionPlan": "pro",
    "maxUsers": 25,
    "maxProjects": 15,
    "stats": {
      "totalUsers": 3,
      "totalProjects": 2,
      "totalTasks": 10
    }
  }
}
```

### PUT /api/tenants/:tenantId
Update tenant details (admin only).

**Request Body:**
```json
{
  "name": "Updated Company Name"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Tenant updated successfully"
}
```

### GET /api/tenants
List all tenants (super_admin only).

**Query Parameters:**
- `page` (integer, default: 1)
- `limit` (integer, default: 10, max: 100)
- `status` (enum: active, suspended, trial)
- `subscriptionPlan` (enum: free, pro, enterprise)

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "tenants": [...],
    "pagination": {
      "currentPage": 1,
      "totalPages": 1,
      "totalTenants": 5
    }
  }
}
```

---

## User Management APIs

### POST /api/tenants/:tenantId/users
Create new user in tenant (admin only).

**Request Body:**
```json
{
  "email": "newuser@demo.com",
  "password": "UserPass@123",
  "fullName": "New User",
  "role": "user"
}
```

**Response (201 Created):**
```json
{
  "success": true,
  "message": "User created successfully",
  "data": {
    "id": "uuid",
    "email": "newuser@demo.com",
    "fullName": "New User",
    "role": "user",
    "isActive": true
  }
}
```

### GET /api/tenants/:tenantId/users
List all users in tenant.

**Query Parameters:**
- `search` (string, optional)
- `role` (enum, optional)
- `page` (integer, default: 1)
- `limit` (integer, default: 50)

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "users": [...],
    "total": 3,
    "pagination": {
      "currentPage": 1,
      "totalPages": 1
    }
  }
}
```

### PUT /api/users/:userId
Update user details.

**Request Body:**
```json
{
  "fullName": "Updated Name",
  "role": "user"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "User updated successfully"
}
```

---

## Project Management APIs

### POST /api/tenants/:tenantId/projects
Create new project.

**Request Body:**
```json
{
  "name": "Project Name",
  "description": "Project description"
}
```

**Response (201 Created):**
```json
{
  "success": true,
  "message": "Project created successfully",
  "data": {
    "id": "uuid",
    "name": "Project Name",
    "description": "Project description",
    "status": "active"
  }
}
```

### GET /api/tenants/:tenantId/projects
List all projects in tenant.

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "projects": [...],
    "total": 2
  }
}
```

### GET /api/projects/:projectId
Get project details.

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "id": "uuid",
    "name": "Project Name",
    "description": "Project description",
    "status": "active",
    "createdAt": "2025-12-24T08:00:00Z"
  }
}
```

### PUT /api/projects/:projectId
Update project details.

**Request Body:**
```json
{
  "name": "Updated Project Name",
  "status": "archived"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Project updated successfully"
}
```

### DELETE /api/projects/:projectId
Delete project.

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Project deleted successfully"
}
```

---

## Task Management APIs

### POST /api/projects/:projectId/tasks
Create new task.

**Request Body:**
```json
{
  "title": "Task Title",
  "description": "Task description",
  "priority": "high",
  "status": "todo"
}
```

**Response (201 Created):**
```json
{
  "success": true,
  "message": "Task created successfully",
  "data": {
    "id": "uuid",
    "title": "Task Title",
    "status": "todo",
    "priority": "high"
  }
}
```

### GET /api/projects/:projectId/tasks
List all tasks in project.

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "tasks": [...],
    "total": 5
  }
}
```

### PUT /api/tasks/:taskId
Update task details.

**Request Body:**
```json
{
  "title": "Updated Title",
  "status": "in_progress",
  "priority": "medium"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Task updated successfully"
}
```

### DELETE /api/tasks/:taskId
Delete task.

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Task deleted successfully"
}
```

---

## Error Responses

### 400 Bad Request
```json
{
  "success": false,
  "message": "Invalid request parameters",
  "errors": {
    "fieldName": "Error message"
  }
}
```

### 401 Unauthorized
```json
{
  "success": false,
  "message": "Unauthorized - token missing or invalid"
}
```

### 403 Forbidden
```json
{
  "success": false,
  "message": "Forbidden - insufficient permissions"
}
```

### 404 Not Found
```json
{
  "success": false,
  "message": "Resource not found"
}
```

### 409 Conflict
```json
{
  "success": false,
  "message": "Resource already exists"
}
```

### 500 Internal Server Error
```json
{
  "success": false,
  "message": "Internal server error"
}
```
