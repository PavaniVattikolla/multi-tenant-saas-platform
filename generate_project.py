#!/usr/bin/env python3
import os
import json
from pathlib import Path

PROJECT_ROOT = Path.cwd()

# Create all required directories
DIRS = [
    'database/migrations',
    'database/seeds',
    'backend/src/controllers',
    'backend/src/models',
    'backend/src/routes',
    'backend/src/middleware',
    'backend/src/utils',
    'backend/src/config',
    'frontend/src/pages',
    'frontend/src/components',
    'frontend/src/services',
    'frontend/src/hooks',
    'frontend/public',
    'docs/images',
    'config'
]

for dir_path in DIRS:
    Path(dir_path).mkdir(parents=True, exist_ok=True)
    print(f"✓ Created directory: {dir_path}")

# DATABASE MIGRATION FILES
migrations = {
    'database/migrations/001_create_tenants.sql': '''-- Create tenants table
CREATE TABLE IF NOT EXISTS tenants (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    subdomain VARCHAR(255) UNIQUE NOT NULL,
    status VARCHAR(50) DEFAULT 'active',
    subscription_plan VARCHAR(50) DEFAULT 'free',
    max_users INTEGER DEFAULT 5,
    max_projects INTEGER DEFAULT 3,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_tenants_subdomain ON tenants(subdomain);
''',

    'database/migrations/002_create_users.sql': '''-- Create users table
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID REFERENCES tenants(id) ON DELETE CASCADE,
    email VARCHAR(255) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    role VARCHAR(50) DEFAULT 'user',
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(tenant_id, email)
);
CREATE INDEX IF NOT EXISTS idx_users_tenant_id ON users(tenant_id);
CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
CREATE INDEX IF NOT EXISTS idx_users_role ON users(role);
''',

    'database/migrations/003_create_projects.sql': '''-- Create projects table
CREATE TABLE IF NOT EXISTS projects (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(50) DEFAULT 'active',
    created_by UUID REFERENCES users(id) ON DELETE SET NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_projects_tenant_id ON projects(tenant_id);
CREATE INDEX IF NOT EXISTS idx_projects_created_by ON projects(created_by);
CREATE INDEX IF NOT EXISTS idx_projects_status ON projects(status);
''',

    'database/migrations/004_create_tasks.sql': '''-- Create tasks table
CREATE TABLE IF NOT EXISTS tasks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    project_id UUID NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(50) DEFAULT 'todo',
    priority VARCHAR(50) DEFAULT 'medium',
    assigned_to UUID REFERENCES users(id) ON DELETE SET NULL,
    due_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_tasks_project_id ON tasks(project_id);
CREATE INDEX IF NOT EXISTS idx_tasks_tenant_id ON tasks(tenant_id);
CREATE INDEX IF NOT EXISTS idx_tasks_assigned_to ON tasks(assigned_to);
CREATE INDEX IF NOT EXISTS idx_tasks_status ON tasks(status);
CREATE INDEX IF NOT EXISTS idx_tasks_priority ON tasks(priority);
''',

    'database/migrations/005_create_audit_logs.sql': '''-- Create audit_logs table
CREATE TABLE IF NOT EXISTS audit_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    user_id UUID REFERENCES users(id) ON DELETE SET NULL,
    action VARCHAR(255) NOT NULL,
    entity_type VARCHAR(255),
    entity_id VARCHAR(255),
    ip_address VARCHAR(45),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_audit_logs_tenant_id ON audit_logs(tenant_id);
CREATE INDEX IF NOT EXISTS idx_audit_logs_user_id ON audit_logs(user_id);
CREATE INDEX IF NOT EXISTS idx_audit_logs_action ON audit_logs(action);
CREATE INDEX IF NOT EXISTS idx_audit_logs_created_at ON audit_logs(created_at);
''',

    'database/seeds/seed_data.sql': '''-- Seed data
-- Password hashes: Admin@123 = $2b$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcg7b3XeKeUxWdeS86E36UxeOU82

INSERT INTO tenants (id, name, subdomain, status, subscription_plan, max_users, max_projects) VALUES
('550e8400-e29b-41d4-a716-446655440002', 'Demo Company', 'demo', 'active', 'pro', 25, 15)
ON CONFLICT DO NOTHING;

INSERT INTO users (id, tenant_id, email, password_hash, full_name, role, is_active) VALUES
('550e8400-e29b-41d4-a716-446655440001', NULL, 'superadmin@system.com', '$2b$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcg7b3XeKeUxWdeS86E36UxeOU82', 'Super Admin', 'super_admin', true),
('550e8400-e29b-41d4-a716-446655440003', '550e8400-e29b-41d4-a716-446655440002', 'admin@demo.com', '$2b$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcg7b3XeKeUxWdeS86E36UxeOU82', 'Demo Admin', 'tenant_admin', true),
('550e8400-e29b-41d4-a716-446655440004', '550e8400-e29b-41d4-a716-446655440002', 'user1@demo.com', '$2b$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcg7b3XeKeUxWdeS86E36UxeOU82', 'User One', 'user', true),
('550e8400-e29b-41d4-a716-446655440005', '550e8400-e29b-41d4-a716-446655440002', 'user2@demo.com', '$2b$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcg7b3XeKeUxWdeS86E36UxeOU82', 'User Two', 'user', true)
ON CONFLICT DO NOTHING;

INSERT INTO projects (id, tenant_id, name, description, status, created_by) VALUES
('550e8400-e29b-41d4-a716-446655440006', '550e8400-e29b-41d4-a716-446655440002', 'Website Redesign', 'Complete redesign of company website', 'active', '550e8400-e29b-41d4-a716-446655440003'),
('550e8400-e29b-41d4-a716-446655440007', '550e8400-e29b-41d4-a716-446655440002', 'Mobile App', 'Build native mobile application', 'active', '550e8400-e29b-41d4-a716-446655440003')
ON CONFLICT DO NOTHING;

INSERT INTO tasks (id, project_id, tenant_id, title, description, status, priority, assigned_to, due_date) VALUES
('550e8400-e29b-41d4-a716-446655440008', '550e8400-e29b-41d4-a716-446655440006', '550e8400-e29b-41d4-a716-446655440002', 'Design mockups', 'Create high-fidelity design', 'completed', 'high', '550e8400-e29b-41d4-a716-446655440004', '2025-12-25'),
('550e8400-e29b-41d4-a716-446655440009', '550e8400-e29b-41d4-a716-446655440006', '550e8400-e29b-41d4-a716-446655440002', 'Frontend', 'Code the frontend', 'in_progress', 'high', '550e8400-e29b-41d4-a716-446655440004', '2025-12-28'),
('550e8400-e29b-41d4-a716-446655440010', '550e8400-e29b-41d4-a716-446655440006', '550e8400-e29b-41d4-a716-446655440002', 'APIs', 'Build backend APIs', 'todo', 'medium', '550e8400-e29b-41d4-a716-446655440005', '2025-12-30'),
('550e8400-e29b-41d4-a716-446655440011', '550e8400-e29b-41d4-a716-446655440007', '550e8400-e29b-41d4-a716-446655440002', 'Dev Setup', 'Configure dev tools', 'completed', 'low', '550e8400-e29b-41d4-a716-446655440005', '2025-12-26'),
('550e8400-e29b-41d4-a716-446655440012', '550e8400-e29b-41d4-a716-446655440007', '550e8400-e29b-41d4-a716-446655440002', 'App UI', 'Design app interface', 'todo', 'medium', '550e8400-e29b-41d4-a716-446655440004', '2025-01-05')
ON CONFLICT DO NOTHING;
'''
}

# Write migration and seed files
for file_path, content in migrations.items():
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"✓ Created: {file_path}")

print("\n✅ Database setup files created successfully!")
