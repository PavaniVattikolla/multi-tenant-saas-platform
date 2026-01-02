# Technical Specification

## Project Structure

### Root Directory

```
multi-tenant-saas-platform/
├── backend/                 # Backend Node.js application
├── frontend/               # Frontend React application
├── database/              # Database related files
├── config/                # Configuration files
├── docs/                  # Documentation
├── docker-compose.yml     # Docker Compose configuration
├── .env                   # Environment variables
├── .env.example          # Environment variables template
├── README.md             # Project documentation
├── README_DOCKER.md      # Docker setup guide
└── submission.json       # Submission metadata
```

### Backend Structure

```
backend/
├── src/
│   ├── controllers/          # Route controllers
│   │   ├── authController.js
│   │   ├── tenantController.js
│   │   ├── userController.js
│   │   ├── projectController.js
│   │   ├── taskController.js
│   │   └── auditController.js
│   ├── middleware/           # Express middleware
│   │   ├── auth.js          # Authentication middleware
│   │   ├── authorization.js # Authorization middleware
│   │   ├── tenantContext.js # Tenant isolation
│   │   └── errorHandler.js  # Error handling
│   ├── models/              # Data models
│   │   ├── Tenant.js
│   │   ├── User.js
│   │   ├── Project.js
│   │   ├── Task.js
│   │   └── AuditLog.js
│   ├── routes/              # API routes
│   │   ├── authRoutes.js
│   │   ├── tenantRoutes.js
│   │   ├── userRoutes.js
│   │   ├── projectRoutes.js
│   │   ├── taskRoutes.js
│   │   └── healthRoutes.js
│   ├── utils/               # Utility functions
│   │   ├── logger.js
│   │   ├── validator.js
│   │   └── helpers.js
│   └── config/              # Configuration
│       └── database.js
├── database/
│   ├── migrations/          # Database migrations
│   │   ├── 001_create_tenants.sql
│   │   ├── 002_create_users.sql
│   │   ├── 003_create_projects.sql
│   │   ├── 004_create_tasks.sql
│   │   └── 005_create_audit_logs.sql
│   └── seeds/              # Seed data
│       └── seed_data.sql
├── Dockerfile              # Backend Docker configuration
├── package.json            # Node.js dependencies
├── server.js              # Entry point
└── .env                   # Backend environment variables
```

### Frontend Structure

```
frontend/
├── src/
│   ├── components/          # React components
│   │   ├── Auth/
│   │   │   ├── Login.js
│   │   │   └── Register.js
│   │   ├── Dashboard/
│   │   │   └── Dashboard.js
│   │   ├── Projects/
│   │   │   ├── ProjectList.js
│   │   │   ├── ProjectForm.js
│   │   │   └── ProjectDetails.js
│   │   ├── Tasks/
│   │   │   ├── TaskList.js
│   │   │   ├── TaskForm.js
│   │   │   └── TaskDetails.js
│   │   ├── Users/
│   │   │   ├── UserList.js
│   │   │   └── UserForm.js
│   │   └── Common/
│   │       ├── Header.js
│   │       ├── Sidebar.js
│   │       └── Footer.js
│   ├── services/            # API services
│   │   ├── authService.js
│   │   ├── tenantService.js
│   │   ├── userService.js
│   │   ├── projectService.js
│   │   └── taskService.js
│   ├── utils/               # Utility functions
│   │   ├── api.js
│   │   └── helpers.js
│   ├── context/             # React context
│   │   └── AuthContext.js
│   ├── App.js              # Main App component
│   └── index.js            # Entry point
├── public/
│   ├── index.html
│   └── favicon.ico
├── Dockerfile              # Frontend Docker configuration
└── package.json            # React dependencies
```

## Development Setup

### Prerequisites

- Node.js 16.x or higher
- PostgreSQL 15.x
- Docker and Docker Compose (for containerized setup)
- Git

### Local Development (Without Docker)

#### 1. Database Setup

```bash
# Install PostgreSQL
# Create database
createdb multi_tenant_saas

# Run migrations
psql -d multi_tenant_saas -f backend/database/migrations/001_create_tenants.sql
psql -d multi_tenant_saas -f backend/database/migrations/002_create_users.sql
psql -d multi_tenant_saas -f backend/database/migrations/003_create_projects.sql
psql -d multi_tenant_saas -f backend/database/migrations/004_create_tasks.sql
psql -d multi_tenant_saas -f backend/database/migrations/005_create_audit_logs.sql

# Load seed data
psql -d multi_tenant_saas -f backend/database/seeds/seed_data.sql
```

#### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Install dependencies
npm install

# Create .env file
cp .env.example .env

# Edit .env with your configuration
# Start development server
npm run dev
```

#### 3. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Create .env file
cp .env.example .env

# Edit .env with backend API URL
# Start development server
npm start
```

### Docker Development Setup

#### Prerequisites
- Docker Desktop installed
- Docker Compose installed

#### Setup Steps

```bash
# Clone repository
git clone https://github.com/PavaniVattikolla/multi-tenant-saas-platform.git
cd multi-tenant-saas-platform

# Create .env file (if not present)
cp .env.example .env

# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop all services
docker-compose down

# Rebuild and restart
docker-compose up -d --build
```

#### Docker Services

**Database Service:**
- Container: `multi-tenant-db`
- Port: `5432:5432`
- Volume: `postgres_data`
- Health Check: PostgreSQL ready check

**Backend Service:**
- Container: `multi-tenant-backend`
- Port: `5000:5000`
- Depends On: database (with health check)
- Auto-restart: yes

**Frontend Service:**
- Container: `multi-tenant-frontend`
- Port: `3000:3000`
- Depends On: backend
- Auto-restart: yes

#### Accessing Services

- Frontend: http://localhost:3000
- Backend API: http://localhost:5000
- Database: localhost:5432
- Health Check: http://localhost:5000/api/health

## Environment Variables

### Backend Environment Variables (.env)

```env
# Database Configuration
DB_USER=tenant_user
DB_PASSWORD=tenant_password
DB_NAME=multi_tenant_saas
DB_HOST=database
DB_PORT=5432

# Backend Configuration
NODE_ENV=development
PORT=5000
JWT_SECRET=your-secret-key-change-in-production
JWT_EXPIRY=24h
CORS_ORIGIN=http://localhost:3000,http://frontend:3000

# Frontend Configuration
REACT_APP_API_URL=http://localhost:5000/api
REACT_APP_ENV=development
```

### Production Environment Variables

For production deployment, ensure you:
- Use strong JWT_SECRET
- Set NODE_ENV=production
- Configure proper CORS_ORIGIN
- Use secure database credentials
- Enable HTTPS

## Database Migrations

### Automatic Migration (Docker)

Migrations run automatically when the database container starts for the first time. Migration files are mounted to `/docker-entrypoint-initdb.d/` in the database container.

### Manual Migration

If you need to run migrations manually:

```bash
# Connect to database container
docker exec -it multi-tenant-db psql -U tenant_user -d multi_tenant_saas

# Run migration files
\i /docker-entrypoint-initdb.d/001_create_tenants.sql
\i /docker-entrypoint-initdb.d/002_create_users.sql
# ... continue for all migration files
```

## Seed Data

Seed data is automatically loaded after migrations complete. The seed data includes:

- 1 Super Admin user
- 1 Demo Tenant
- 1 Tenant Admin user
- 2 Regular users
- 2 Sample projects
- 3 Sample tasks

### Seed Data Credentials

All credentials are documented in `submission.json` under the `testCredentials` section.

## API Testing

### Using Postman

1. Import the Postman collection (if provided)
2. Set environment variables:
   - `base_url`: http://localhost:5000/api
   - `token`: (will be set automatically after login)

### Using cURL

```bash
# Health Check
curl http://localhost:5000/api/health

# Register Tenant
curl -X POST http://localhost:5000/api/auth/register-tenant \
  -H "Content-Type: application/json" \
  -d '{
    "tenantName": "Test Company",
    "subdomain": "test",
    "adminEmail": "admin@test.com",
    "adminPassword": "Test@123",
    "fullName": "Test Admin"
  }'

# Login
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "admin@test.com",
    "password": "Test@123"
  }'
```

## Troubleshooting

### Common Issues

#### Port Already in Use

```bash
# Check what's using the port
lsof -i :5000
lsof -i :3000
lsof -i :5432

# Kill the process or change ports in docker-compose.yml
```

#### Database Connection Failed

```bash
# Check database logs
docker logs multi-tenant-db

# Verify database is running
docker ps | grep multi-tenant-db

# Test database connection
docker exec -it multi-tenant-db psql -U tenant_user -d multi_tenant_saas -c "\dt"
```

#### Backend Not Starting

```bash
# Check backend logs
docker logs multi-tenant-backend

# Restart backend service
docker-compose restart backend

# Rebuild backend
docker-compose up -d --build backend
```

#### Frontend Build Fails

```bash
# Check frontend logs
docker logs multi-tenant-frontend

# Clear node_modules and rebuild
docker-compose down
docker-compose up -d --build frontend
```

## Testing

### Unit Tests

```bash
# Backend tests
cd backend
npm test

# Frontend tests
cd frontend
npm test
```

### Integration Tests

```bash
# Run integration tests
npm run test:integration
```

## Code Quality

### Linting

```bash
# Backend
cd backend
npm run lint

# Frontend
cd frontend
npm run lint
```

### Formatting

```bash
# Format code with Prettier
npm run format
```

## Deployment

### Production Build

```bash
# Build all services
docker-compose -f docker-compose.prod.yml build

# Start in production mode
docker-compose -f docker-compose.prod.yml up -d
```

### Cloud Deployment

For cloud deployment (AWS, Azure, GCP), consider:
- Using managed database services (RDS, Azure Database, Cloud SQL)
- Container orchestration (ECS, AKS, GKE)
- Load balancing
- Auto-scaling
- CDN for frontend assets
- Environment-specific configurations

## Security Best Practices

- Never commit .env files with sensitive data
- Use strong JWT secrets
- Implement rate limiting
- Enable CORS only for trusted origins
- Use HTTPS in production
- Regular security updates
- Input validation on all endpoints
- SQL injection prevention through parameterized queries
- XSS protection
- CSRF protection

## Performance Optimization

- Database indexing on frequently queried columns
- Connection pooling
- Caching with Redis (future enhancement)
- Lazy loading in frontend
- Code splitting
- Image optimization
- Compression middleware
