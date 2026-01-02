# Testing Guide

## Running Tests

### Backend Tests

```bash
cd backend
npm test
```

### Frontend Tests

```bash
cd frontend
npm test
```

## Test Coverage

- Unit tests for controllers
- Integration tests for API endpoints
- Authentication flow tests
- Multi-tenancy isolation tests
- RBAC permission tests

## Manual Testing

### Test Accounts

Use credentials from `submission.json`:

- Super Admin: superadmin@system.com
- Tenant Admin: admin@demo.com
- Regular User: user1@demo.com

### Test Scenarios

1. **Tenant Registration**
   - Register new tenant
   - Verify tenant isolation

2. **User Management**
   - Create users with different roles
   - Test permission boundaries

3. **Project & Task Management**
   - Create, update, delete projects
   - Assign tasks to users
   - Verify status updates

4. **Security Testing**
   - Test cross-tenant data access (should fail)
   - Verify JWT token expiration
   - Test SQL injection prevention
