# Multi-Tenant SaaS Platform

A production-ready multi-tenant SaaS platform with authentication, tenant isolation, role-based access control (RBAC), project management, task tracking, and comprehensive audit logging.

## Features

- **Multi-Tenancy**: Complete tenant isolation with subdomain-based routing
- **Authentication & Authorization**: JWT-based authentication with role-based access control
- **User Management**: User registration, login, and profile management
- **Project Management**: Create, update, and manage projects within tenants
- **Task Tracking**: Assign and track tasks with status management
- **Audit Logging**: Comprehensive activity logging for compliance
- **RESTful API**: Well-documented API endpoints
- **Docker Support**: Complete Docker and Docker Compose setup

## Tech Stack

### Backend
- Node.js with Express.js
- PostgreSQL database
- JWT for authentication
- Sequelize ORM

### Frontend
- React.js
- Modern UI components
- API integration

### DevOps
- Docker & Docker Compose
- Environment-based configuration

## Prerequisites

Before installation, ensure you have:

- **Node.js** 16.x or higher
- **npm** or **yarn**
- **PostgreSQL** 13.x or higher
- **Docker** 20.10+ and **Docker Compose** 2.0+ (for Docker setup)
- **Git**

## Installation

### Option 1: Docker Installation (Recommended)

The fastest way to get started is using Docker:

```bash
# Clone the repository
git clone https://github.com/PavaniVattikolla/multi-tenant-saas-platform.git
cd multi-tenant-saas-platform

# Start all services with Docker Compose
docker-compose up -d

# Wait for services to be healthy (10-15 seconds)
# Check logs
docker-compose logs -f
```

For detailed Docker instructions, see [README_DOCKER.md](README_DOCKER.md).

### Option 2: Manual Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/PavaniVattikolla/multi-tenant-saas-platform.git
cd multi-tenant-saas-platform
```

#### 2. Database Setup

```bash
# Create PostgreSQL database
creatdb multi_tenant_saas

# Or using psql
psql -U postgres
CREATE DATABASE multi_tenant_saas;
\q
```

#### 3. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Install dependencies
npm install

# Create .env file from example
cp ../.env.example ../.env

# Edit .env with your database credentials
# Run database migrations
npm run migrate

# Seed database with initial data
npm run seed

# Start backend server
npm start
# Backend will run on http://localhost:5000
```

#### 4. Frontend Setup

```bash
# Open new terminal
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start frontend development server
npm start
# Frontend will run on http://localhost:3000
```

## Environment Configuration

Create a `.env` file in the root directory (or copy from `.env.example`):

```env
# Database Configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME=multi_tenant_saas
DB_USER=tenant_user
DB_PASSWORD=tenant_password

# Server Configuration
NODE_ENV=development
PORT=5000

# JWT Configuration
JWT_SECRET=your-secret-key-change-in-production
JWT_EXPIRY=24h

# CORS Configuration
CORS_ORIGIN=http://localhost:3000,http://frontend:3000

# Frontend Configuration
REACT_APP_API_URL=http://localhost:5000/api
REACT_APP_ENV=development
```

**Important**: Change `JWT_SECRET` and `DB_PASSWORD` to strong values for production.

## Accessing the Application

Once installation is complete:

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:5000
- **API Health Check**: http://localhost:5000/api/health
- **API Documentation**: http://localhost:5000/api

## Test Credentials

### Super Admin Account
- **Email**: `superadmin@system.com`
- **Password**: `Admin@123`
- **Role**: System administrator (access all tenants)

### Demo Tenant Admin
- **Email**: `admin@demo.com`
- **Password**: `Demo@123`
- **Tenant**: Demo Company
- **Role**: Tenant administrator

### Demo Regular Users
- **User 1**: `user1@demo.com` / `User@123`
- **User 2**: `user2@demo.com` / `User@123`

## Project Structure

```
multi-tenant-saas-platform/
├── backend/           # Node.js backend application
│   ├── src/
│   ├── Dockerfile
│   └── package.json
├── frontend/          # React frontend application
│   ├── src/
│   ├── Dockerfile
│   └── package.json
├── database/          # Database migrations and seeds
├── docs/              # Documentation
│   ├── API.md
│   ├── architecture.md
│   ├── PRD.md
│   ├── research.md
│   └── technical-spec.md
├── config/            # Configuration files
├── docker-compose.yml # Docker Compose configuration
├── .env.example       # Environment variables template
└── README.md          # This file
```

## Development

### Running Tests

```bash
# Backend tests
cd backend
npm test

# Frontend tests
cd frontend
npm test
```

### Code Linting

```bash
# Backend linting
cd backend
npm run lint

# Frontend linting
cd frontend
npm run lint
```

## API Documentation

Detailed API documentation is available in [docs/API.md](docs/API.md).

Key endpoints:
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `GET /api/users` - List users
- `GET /api/projects` - List projects
- `GET /api/tasks` - List tasks
- `GET /api/audit-logs` - View audit logs

## Documentation

- [API Documentation](docs/API.md)
- [Architecture Overview](docs/architecture.md)
- [Product Requirements](docs/PRD.md)
- [Research Document](docs/research.md)
- [Technical Specifications](docs/technical-spec.md)
- [Docker Setup Guide](README_DOCKER.md)

## Troubleshooting

### Common Issues

**Port Already in Use**
```bash
# Check what's using the port
lsof -i :5000  # Backend
lsof -i :3000  # Frontend

# Kill the process
kill -9 <PID>
```

**Database Connection Failed**
```bash
# Check PostgreSQL is running
pg_isready

# Verify database exists
psql -U postgres -l

# Check credentials in .env file
```

**Docker Issues**
```bash
# Clean restart
docker-compose down -v
docker-compose up -d --build

# View logs
docker-compose logs -f
```

## Deployment

For production deployment:

1. Use environment-specific configuration
2. Set strong passwords and secrets
3. Enable HTTPS/TLS
4. Use managed database services (RDS, Cloud SQL)
5. Implement proper logging and monitoring
6. Set up CI/CD pipeline
7. Use container registries

See [README_DOCKER.md](README_DOCKER.md) for production Docker deployment details.

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Write tests
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For issues or questions:
1. Check the documentation in the `docs/` folder
2. Review troubleshooting section above
3. Check existing issues on GitHub
4. Create a new issue with detailed information
