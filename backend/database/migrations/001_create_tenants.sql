-- Create ENUM types for tenant status and subscription plans
CREATE TYPE tenant_status AS ENUM ('active', 'suspended', 'trial');
CREATE TYPE subscription_plan AS ENUM ('free', 'pro', 'enterprise');

-- Create tenants table
CREATE TABLE tenants (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    subdomain VARCHAR(255) UNIQUE NOT NULL,
    status tenant_status DEFAULT 'active',
    subscription_plan subscription_plan DEFAULT 'free',
    max_users INTEGER,
    max_projects INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Add index on subdomain for faster lookups
CREATE INDEX idx_tenants_subdomain ON tenants(subdomain);

-- Down migration (commented for reference)
-- DROP TABLE IF EXISTS tenants CASCADE;
-- DROP TYPE IF EXISTS subscription_plan;
-- DROP TYPE IF EXISTS tenant_status;
