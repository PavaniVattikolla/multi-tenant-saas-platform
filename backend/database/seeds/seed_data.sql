-- Insert super admin user (tenant_id = NULL)
INSERT INTO users (id, tenant_id, email, password_hash, full_name, role, is_active)
VALUES (
    '550e8400-e29b-41d4-a716-446655440001',
    NULL,
    'superadmin@system.com',
    '$2b$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcg7b3XeKeUxWdeS86E36UxeOU82', -- hashed: Admin@123 using bcrypt
    'Super Admin',
    'super_admin',
    true
);

-- Insert demo tenant
INSERT INTO tenants (id, name, subdomain, status, subscription_plan, max_users, max_projects)
VALUES (
    '550e8400-e29b-41d4-a716-446655440002',
    'Demo Company',
    'demo',
    'active',
    'pro',
    25,
    15
);

-- Insert tenant admin for demo company
INSERT INTO users (id, tenant_id, email, password_hash, full_name, role, is_active)
VALUES (
    '550e8400-e29b-41d4-a716-446655440003',
    '550e8400-e29b-41d4-a716-446655440002',
    'admin@demo.com',
    '$2b$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcg7b3XeKeUxWdeS86E36UxeOU82', -- hashed: Demo@123
    'Demo Admin',
    'tenant_admin',
    true
);

-- Insert regular users
INSERT INTO users (id, tenant_id, email, password_hash, full_name, role, is_active)
VALUES 
(
    '550e8400-e29b-41d4-a716-446655440004',
    '550e8400-e29b-41d4-a716-446655440002',
    'user1@demo.com',
    '$2b$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcg7b3XeKeUxWdeS86E36UxeOU82', -- hashed: User@123
    'User One',
    'user',
    true
),
(
    '550e8400-e29b-41d4-a716-446655440005',
    '550e8400-e29b-41d4-a716-446655440002',
    'user2@demo.com',
    '$2b$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcg7b3XeKeUxWdeS86E36UxeOU82', -- hashed: User@123
    'User Two',
    'user',
    true
);

-- Insert sample projects
INSERT INTO projects (id, tenant_id, name, description, status, created_by)
VALUES 
(
    '550e8400-e29b-41d4-a716-446655440006',
    '550e8400-e29b-41d4-a716-446655440002',
    'Website Redesign',
    'Complete redesign of company website',
    'active',
    '550e8400-e29b-41d4-a716-446655440003'
),
(
    '550e8400-e29b-41d4-a716-446655440007',
    '550e8400-e29b-41d4-a716-446655440002',
    'Mobile App Development',
    'Build native mobile application',
    'active',
    '550e8400-e29b-41d4-a716-446655440003'
);

-- Insert sample tasks
INSERT INTO tasks (id, project_id, tenant_id, title, description, status, priority, assigned_to, due_date)
VALUES 
(
    '550e8400-e29b-41d4-a716-446655440008',
    '550e8400-e29b-41d4-a716-446655440006',
    '550e8400-e29b-41d4-a716-446655440002',
    'Design mockups',
    'Create high-fidelity design mockups',
    'completed',
    'high',
    '550e8400-e29b-41d4-a716-446655440004',
    '2025-12-25'
),
(
    '550e8400-e29b-41d4-a716-446655440009',
    '550e8400-e29b-41d4-a716-446655440006',
    '550e8400-e29b-41d4-a716-446655440002',
    'Implement frontend',
    'Code the frontend using React',
    'in_progress',
    'high',
    '550e8400-e29b-41d4-a716-446655440004',
    '2025-12-28'
),
(
    '550e8400-e29b-41d4-a716-446655440010',
    '550e8400-e29b-41d4-a716-446655440006',
    '550e8400-e29b-41d4-a716-446655440002',
    'API Development',
    'Build backend APIs',
    'todo',
    'medium',
    '550e8400-e29b-41d4-a716-446655440005',
    '2025-12-30'
),
(
    '550e8400-e29b-41d4-a716-446655440011',
    '550e8400-e29b-41d4-a716-446655440007',
    '550e8400-e29b-41d4-a716-446655440002',
    'Setup development environment',
    'Configure mobile dev tools',
    'completed',
    'low',
    '550e8400-e29b-41d4-a716-446655440005',
    '2025-12-26'
),
(
    '550e8400-e29b-41d4-a716-446655440012',
    '550e8400-e29b-41d4-a716-446655440007',
    '550e8400-e29b-41d4-a716-446655440002',
    'App UI design',
    'Design app interface',
    'todo',
    'medium',
    '550e8400-e29b-41d4-a716-446655440004',
    '2025-01-05'
);
