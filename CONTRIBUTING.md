# Contributing to record-shelf

Thank you for your interest in contributing to record-shelf! This document provides guidelines and information for contributors.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- A Discogs account and API token for testing

### Development Setup

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/bryankemp/record-shelf.git
   cd record-shelf
   ```

3. Set up the development environment:
   ```bash
   make setup
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install pre-commit hooks:
   ```bash
   make pre-commit
   ```

## Development Workflow

### Running Tests

```bash
# Run all tests
make test

# Run tests with coverage
make test-cov

# Run quick tests
make qtest
```

### Code Quality

```bash
# Run all linting and formatting
make lint

# Format code
make format

# Type checking
make type-check

# Security checks
make security

# Run all development checks
make dev-test
```

### Documentation

```bash
# Build documentation
make docs

# Serve documentation locally
make docs-serve

# Rebuild documentation
make docs-rebuild
```

## Contribution Guidelines

### Code Style

- Follow PEP 8 style guidelines
- Use Black for code formatting
- Use isort for import sorting
- Include type hints for all functions and methods
- Write descriptive docstrings using Google style

### Testing

- Write tests for all new features and bug fixes
- Maintain or improve test coverage
- Use pytest for testing
- Mock external API calls in tests

### Commit Messages

Use conventional commit format:

- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `style:` for formatting changes
- `refactor:` for code refactoring
- `test:` for test changes
- `chore:` for maintenance tasks

Example: `feat: add support for wantlist export`

### Pull Requests

1. Create a feature branch: `git checkout -b feature/your-feature-name`
2. Make your changes and commit them
3. Push to your fork: `git push origin feature/your-feature-name`
4. Create a pull request on GitHub

#### Pull Request Requirements

- [ ] All tests pass
- [ ] Code coverage is maintained or improved
- [ ] Documentation is updated if needed
- [ ] CHANGELOG.md is updated
- [ ] Code follows project style guidelines
- [ ] Commit messages follow conventional format

## Reporting Issues

### Bug Reports

When reporting bugs, please include:

- Python version
- Operating system
- record-shelf version
- Steps to reproduce
- Expected vs actual behavior
- Error messages/stack traces
- Sample data (if applicable, anonymized)

### Feature Requests

For feature requests, please:

- Describe the feature and its use case
- Explain why it would be beneficial
- Provide examples of how it would work
- Consider implementation complexity

## Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). By participating, you agree to uphold this code.

## Questions?

If you have questions about contributing, please:

- Check existing issues and discussions
- Create a new issue with the "question" label
- Reach out to the maintainers

Thank you for contributing to record-shelf!

