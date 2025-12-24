-- Seed Super Admin User (bcrypt hash of "Admin@123")
INSERT INTO users (id, tenant_id, email, password_hash, full_name, role, is_active) 
VALUES (
  '00000000-0000-0000-0000-000000000001',
  NULL,
  'superadmin@system.com',
  '$2b$10$9EixZaYVK1fsbw1ZfbX3BeXDlH.PKZbv5H8KnzzVgXXbVxmva.pFm',
  'Super Admin',
  'super_admin',
  true
) ON CONFLICT DO NOTHING;

-- Seed Demo Tenant
INSERT INTO tenants (id, name, subdomain, status, subscription_plan, max_users, max_projects)
VALUES (
  '11111111-1111-1111-1111-111111111111',
  'Demo Company',
  'demo',
  'active',
  'pro',
  25,
  15
) ON CONFLICT DO NOTHING;

-- Seed Tenant Admin (bcrypt hash of "Demo@123")
INSERT INTO users (id, tenant_id, email, password_hash, full_name, role, is_active)
VALUES (
  '22222222-2222-2222-2222-222222222222',
  '11111111-1111-1111-1111-111111111111',
  'admin@demo.com',
  '$2b$10$6W4UxZPk9VfLIvVLBMcxcOjP8EyO5Z.8aHNiD6JAO5cKqF6.pCTPK',
  'Admin User',
  'tenant_admin',
  true
) ON CONFLICT DO NOTHING;

-- Seed Regular Users (bcrypt hash of "User@123")
INSERT INTO users (id, tenant_id, email, password_hash, full_name, role, is_active)
VALUES
  ('33333333-3333-3333-3333-333333333333', '11111111-1111-1111-1111-111111111111', 'user1@demo.com', '$2b$10$6W4UxZPk9VfLIvVLBMcxcOjP8EyO5Z.8aHNiD6JAO5cKqF6.pCTpK', 'User One', 'user', true),
  ('44444444-4444-4444-4444-444444444444', '11111111-1111-1111-1111-111111111111', 'user2@demo.com', '$2b$10$6W4UxZPk9VfLIvVLBMcxcOjP8EyO5Z.8aHNiD6JAO5cKqF6.pCTpK', 'User Two', 'user', true)
ON CONFLICT DO NOTHING;

-- Seed Projects
INSERT INTO projects (id, tenant_id, name, description, status, created_by)
VALUES
  ('55555555-5555-5555-5555-555555555555', '11111111-1111-1111-1111-111111111111', 'Project Alpha', 'First demo project', 'active', '22222222-2222-2222-2222-222222222222'),
  ('66666666-6666-6666-6666-666666666666', '11111111-1111-1111-1111-111111111111', 'Project Beta', 'Second demo project', 'active', '22222222-2222-2222-2222-222222222222')
ON CONFLICT DO NOTHING;

-- Seed Tasks
INSERT INTO tasks (id, project_id, tenant_id, title, description, status, priority, assigned_to)
VALUES
  ('77777777-7777-7777-7777-777777777777', '55555555-5555-5555-5555-555555555555', '11111111-1111-1111-1111-111111111111', 'Task 1', 'First task', 'todo', 'high', '33333333-3333-3333-3333-333333333333'),
  ('88888888-8888-8888-8888-888888888888', '55555555-5555-5555-5555-555555555555', '11111111-1111-1111-1111-111111111111', 'Task 2', 'Second task', 'in_progress', 'medium', '44444444-4444-4444-4444-444444444444'),
  ('99999999-9999-9999-9999-999999999999', '66666666-6666-6666-6666-666666666666', '11111111-1111-1111-1111-111111111111', 'Task 3', 'Third task', 'todo', 'low', NULL),
  ('aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa', '66666666-6666-6666-6666-666666666666', '11111111-1111-1111-1111-111111111111', 'Task 4', 'Fourth task', 'completed', 'high', '33333333-3333-3333-3333-333333333333'),
  ('bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb', '55555555-5555-5555-5555-555555555555', '11111111-1111-1111-1111-111111111111', 'Task 5', 'Fifth task', 'todo', 'medium', '44444444-4444-4444-4444-444444444444')
ON CONFLICT DO NOTHING;
