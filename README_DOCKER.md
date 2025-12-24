# Docker Setup Guide

## Quick Start

The entire Multi-Tenant SaaS Platform can be run with a single Docker command:

```bash
docker-compose up -d
```

This will start all three services:
- **Database** (PostgreSQL) on port 5432
- **Backend API** (Node.js/Express) on port 5000  
- **Frontend** (React) on port 3000

## Prerequisites

- Docker 20.10+
- Docker Compose 2.0+
- Git

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/PavaniVattikolla/multi-tenant-saas-platform.git
cd multi-tenant-saas-platform
```

### 2. Create Environment File

The `.env` file is already included in the repository with default development values:

```bash
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

# Docker Configuration
DOCKER_BUILDKIT=1
```

### 3. Start Docker Compose

```bash
# Start all services
docker-compose up -d

# Wait for services to be healthy (usually 10-15 seconds)
# Check logs
docker-compose logs -f
```

## Accessing the Application

Once all services are running:

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:5000
- **API Documentation**: http://localhost:5000/api (Swagger/API docs)
- **Health Check**: http://localhost:5000/api/health

## Test Credentials

Use these credentials to log in:

### Super Admin Account
- **Email**: `superadmin@system.com`
- **Password**: `Admin@123`
- **Role**: System administrator (can access all tenants)

### Demo Tenant Admin
- **Email**: `admin@demo.com`
- **Password**: `Demo@123`
- **Tenant**: Demo Company (demo subdomain)
- **Role**: Tenant administrator

### Demo Regular Users
- **User 1 Email**: `user1@demo.com`
- **Password**: `User@123`

- **User 2 Email**: `user2@demo.com`
- **Password**: `User@123`

## Docker Compose Structure

### Services

#### Database Service
- **Image**: postgres:15-alpine
- **Container Name**: multi-tenant-db
- **Port Mapping**: 5432:5432
- **Volume**: postgres_data (persistent storage)
- **Health Check**: Enabled

#### Backend Service
- **Build Context**: ./backend
- **Container Name**: multi-tenant-backend
- **Port Mapping**: 5000:5000
- **Volume Mounts**: ./backend/src (live reload)
- **Dependencies**: Waits for database service
- **Health Check**: /api/health endpoint

#### Frontend Service
- **Build Context**: ./frontend
- **Container Name**: multi-tenant-frontend
- **Port Mapping**: 3000:3000
- **Volume Mounts**: ./frontend/src (live reload)
- **Dependencies**: Depends on backend service

## Common Docker Commands

### Start Services
```bash
# Start in background
docker-compose up -d

# Start in foreground (see logs)
docker-compose up
```

### Stop Services
```bash
# Stop all services (keeps data)
docker-compose stop

# Stop and remove containers (keeps data)
docker-compose down

# Stop, remove containers AND delete volumes (cleans everything)
docker-compose down -v
```

### View Logs
```bash
# View all logs
docker-compose logs

# View logs for specific service
docker-compose logs backend
docker-compose logs frontend
docker-compose logs database

# Follow logs in real-time
docker-compose logs -f
```

### Access Running Container
```bash
# Access backend container
docker exec -it multi-tenant-backend sh

# Access database container
docker exec -it multi-tenant-db psql -U tenant_user -d multi_tenant_saas

# Access frontend container
docker exec -it multi-tenant-frontend sh
```

### Database Management
```bash
# Connect to PostgreSQL
docker-compose exec database psql -U tenant_user -d multi_tenant_saas

# View database size
docker-compose exec database du -sh /var/lib/postgresql/data

# Backup database
docker-compose exec database pg_dump -U tenant_user multi_tenant_saas > backup.sql

# Restore database
docker-compose exec -T database psql -U tenant_user multi_tenant_saas < backup.sql
```

## Health Checks

Each service includes health checks:

```bash
# Check service status
docker-compose ps

# Wait for services to be healthy (within 60 seconds)
docker-compose exec backend curl http://localhost:5000/api/health
```

Expected health check response:
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

## Environment Variables

All environment variables are defined in `.env` file. For production:

1. Change `JWT_SECRET` to a strong random value
2. Use strong `DB_PASSWORD`
3. Set `NODE_ENV=production`
4. Update `CORS_ORIGIN` to your domain
5. Use secure database credentials

## Troubleshooting

### Services won't start
```bash
# Check logs
docker-compose logs

# Verify ports aren't in use
lsof -i :3000
lsof -i :5000  
lsof -i :5432

# Clean rebuild
docker-compose down -v
docker-compose up -d --build
```

### Database connection issues
```bash
# Verify database is running
docker-compose ps database

# Check database logs
docker-compose logs database

# Test connection
docker-compose exec database pg_isready -U tenant_user
```

### Port already in use
```bash
# Change ports in docker-compose.yml
# or kill process using the port:
kill -9 $(lsof -t -i:5000)
```

## Performance Optimization

### Enable BuildKit (faster builds)
```bash
export DOCKER_BUILDKIT=1
docker-compose up -d --build
```

### Resource Limits
Edit `docker-compose.yml` to add resource limits:
```yaml
services:
  backend:
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 512M
```

## Production Deployment

For production deployment:

1. Use external managed database (RDS, Cloud SQL, etc.)
2. Use environment-specific `.env.production`
3. Enable HTTPS/TLS
4. Set up proper logging and monitoring
5. Use secrets management (not .env files)
6. Enable container registries (Docker Hub, ECR, etc.)
7. Set up CI/CD pipeline

## Additional Documentation

- [API Documentation](./docs/API.md)
- [Architecture Documentation](./docs/architecture.md)
- [Technical Specification](./docs/technical-spec.md)
- [Research Document](./docs/research.md)
- [Product Requirements](./docs/PRD.md)

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review Docker Compose logs
3. Check application logs
4. Refer to service-specific documentation
