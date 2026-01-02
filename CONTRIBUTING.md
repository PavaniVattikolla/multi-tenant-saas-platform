# Contributing to Multi-Tenant SaaS Platform

Thank you for your interest in contributing to this project! This document provides guidelines for contributing.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment.

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in Issues
2. If not, create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - System information

### Suggesting Enhancements

1. Open an issue describing your enhancement
2. Explain why this enhancement would be useful
3. Provide examples of how it would work

### Pull Requests

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Write or update tests
5. Ensure all tests pass
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to your branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## Development Setup

See the [Technical Specification](docs/technical-spec.md) for detailed setup instructions.

## Coding Standards

### JavaScript/Node.js

- Use ES6+ syntax
- Follow ESLint configuration
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions small and focused

### React

- Use functional components with hooks
- Follow component naming conventions
- Keep components reusable
- Prop validation with PropTypes

### Database

- Use migrations for schema changes
- Always include rollback scripts
- Index frequently queried columns
- Document complex queries

## Commit Messages

Follow conventional commit format:

```
type(scope): subject

body

footer
```

Types:
- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes
- **refactor**: Code refactoring
- **test**: Test updates
- **chore**: Build/tooling changes

## Testing

- Write unit tests for new features
- Ensure integration tests pass
- Test multi-tenancy isolation
- Verify role-based access control

## Documentation

- Update README.md for major changes
- Document API changes
- Add inline code comments
- Update technical specifications

## Questions?

Feel free to open an issue for questions or discussions.
