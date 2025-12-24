// Subscription plan limits
const SUBSCRIPTION_PLANS = {
  free: {
    max_users: 5,
    max_projects: 3,
  },
  pro: {
    max_users: 25,
    max_projects: 15,
  },
  enterprise: {
    max_users: 100,
    max_projects: 50,
  },
};

// User roles
const ROLES = {
  SUPER_ADMIN: 'super_admin',
  TENANT_ADMIN: 'tenant_admin',
  USER: 'user',
};

// Status codes
const STATUS = {
  ACTIVE: 'active',
  SUSPENDED: 'suspended',
  TRIAL: 'trial',
};

// Project status
const PROJECT_STATUS = {
  ACTIVE: 'active',
  ARCHIVED: 'archived',
  COMPLETED: 'completed',
};

// Task status
const TASK_STATUS = {
  TODO: 'todo',
  IN_PROGRESS: 'in_progress',
  COMPLETED: 'completed',
};

// Task priority
const PRIORITY = {
  LOW: 'low',
  MEDIUM: 'medium',
  HIGH: 'high',
};

module.exports = {
  SUBSCRIPTION_PLANS,
  ROLES,
  STATUS,
  PROJECT_STATUS,
  TASK_STATUS,
  PRIORITY,
};
