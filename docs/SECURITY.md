# Security Policy

## Reporting Security Vulnerabilities

If you discover a security vulnerability, please email pavani.vattikolla@example.com

**Please do NOT create public GitHub issues for security vulnerabilities.**

## Security Best Practices

### Authentication
- JWT tokens with 24-hour expiration
- Bcrypt password hashing (10 rounds)
- Secure session management

### Data Protection
- Complete tenant isolation
- Parameterized SQL queries
- Input validation on all endpoints
- CORS configured for trusted origins only

### Infrastructure
- Regular dependency updates
- Docker container security
- Environment variable protection
- HTTPS enforcement in production
