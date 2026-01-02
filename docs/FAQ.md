# Frequently Asked Questions (FAQ)

## General

**Q: What is this project?**
A: A production-ready multi-tenant SaaS platform with authentication, tenant isolation, RBAC, and project/task management.

**Q: What tech stack is used?**
A: Node.js, Express.js, React, PostgreSQL, Docker

## Setup

**Q: How do I run the project?**
A: Run `docker-compose up -d` from the project root.

**Q: What are the default credentials?**
A: Check `submission.json` for all test credentials.

## Multi-Tenancy

**Q: How is tenant isolation achieved?**
A: Every database query filters by tenant_id, ensuring complete data isolation.

**Q: Can I use custom domains per tenant?**
A: Yes, subdomain-based routing is supported.

## Development

**Q: How do I contribute?**
A: See CONTRIBUTING.md for guidelines.

**Q: Where can I find API documentation?**
A: Check docs/API.md for complete API documentation.
