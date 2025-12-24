-- Seed data
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
