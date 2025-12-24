-- Create ENUM type for user roles
CREATE TYPE user_role AS ENUM ('super_admin', 'tenant_admin', 'user');

-- Create users table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID REFERENCES tenants(id) ON DELETE CASCADE,
    email VARCHAR(255) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    role user_role DEFAULT 'user',
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    -- Email unique per tenant (super_admin has NULL tenant_id)
    UNIQUE(tenant_id, email)
);

-- Add indexes for performance
CREATE INDEX idx_users_tenant_id ON users(tenant_id);
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_role ON users(role);

-- Down migration (commented for reference)
-- DROP TABLE IF EXISTS users CASCADE;
-- DROP TYPE IF EXISTS user_role;
