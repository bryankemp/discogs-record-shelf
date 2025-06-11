# Setup Guide: GitHub, PyPI, and Read the Docs Integration

This guide will walk you through setting up your record-shelf project with GitHub, PyPI, and Read the Docs.

## Prerequisites

- [GitHub account](https://github.com) (username: bryankemp)
- [PyPI account](https://pypi.org)
- [Read the Docs account](https://readthedocs.org)
- Git configured locally

## Step 1: GitHub Repository Setup

### 1.1 Create GitHub Repository

1. Go to [GitHub](https://github.com/new)
2. Create a new repository:
   - Repository name: `record-shelf`
   - Description: "A tool for creating custom reports from music collection data"
   - Public repository
   - Don't initialize with README (we already have one)

### 1.2 Push Local Repository

```bash
# Add GitHub remote
git remote add origin https://github.com/bryankemp/record-shelf.git

# Push to GitHub
git push -u origin main
```

### 1.3 Configure Repository Settings

1. Go to repository Settings → General
2. Set default branch to `main`
3. Enable "Discussions" if desired

### 1.4 Set up Branch Protection (Recommended)

1. Go to Settings → Branches
2. Add rule for `main` branch:
   - Require pull request reviews
   - Require status checks to pass (CI)
   - Require branches to be up to date

## Step 2: PyPI Setup

### 2.1 Create PyPI Account

1. Register at [PyPI](https://pypi.org/account/register/)
2. Verify your email address
3. Enable Two-Factor Authentication (recommended)

### 2.2 Generate API Token

1. Go to PyPI Account Settings → API tokens
2. Create a new token:
   - Token name: `record-shelf-github-actions`
   - Scope: "Entire account" (initially, can be restricted later)
3. Copy the token (starts with `pypi-`)

### 2.3 Add PyPI Token to GitHub Secrets

1. Go to your GitHub repository
2. Settings → Secrets and variables → Actions
3. Click "New repository secret"
4. Name: `PYPI_API_TOKEN`
5. Value: Your PyPI token

### 2.4 Create PyPI Project (Optional)

You can reserve your project name:

1. Build and upload a test release:
   ```bash
   make build
   twine upload --repository testpypi dist/*
   ```

## Step 3: Read the Docs Setup

### 3.1 Create Read the Docs Account

1. Go to [Read the Docs](https://readthedocs.org/accounts/signup/)
2. Sign up with GitHub (recommended)
3. Connect your GitHub account

### 3.2 Import Project

1. Go to [Import a Project](https://readthedocs.org/dashboard/import/)
2. Choose "Import from GitHub"
3. Find and select `bryankemp/record-shelf`
4. Click "Next"

### 3.3 Configure Project Settings

1. Project details:
   - Name: `record-shelf`
   - Repository URL: `https://github.com/bryankemp/record-shelf`
   - Default branch: `main`

2. Advanced settings:
   - Programming language: `Python`
   - Documentation type: `Sphinx Html`
   - Requirements file: `docs/requirements.txt`

### 3.4 Build Documentation

1. Trigger first build manually
2. Check build logs for any issues
3. Your docs will be available at: `https://record-shelf.readthedocs.io/`

## Step 4: Environment Setup

### 4.1 GitHub Environments (for Releases)

1. Go to Settings → Environments
2. Create new environment: `release`
3. Add protection rules:
   - Required reviewers (yourself)
   - Deployment branches: `main` only

### 4.2 GitHub Secrets (if needed)

Add any additional secrets your project needs:

- `DISCOGS_TOKEN`: For testing (optional)
- `CODECOV_TOKEN`: For code coverage (optional)

## Step 5: Test the Setup

### 5.1 Test CI Pipeline

1. Make a small change to your code
2. Push to a feature branch
3. Create a pull request
4. Verify that CI checks run successfully

### 5.2 Test Release Pipeline

1. Update version in `pyproject.toml` to `1.0.0`
2. Update `CHANGELOG.md`
3. Create and push a tag:
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```
4. Watch the release workflow run
5. Verify package appears on PyPI
6. Check that GitHub release is created

### 5.3 Test Documentation

1. Push changes to `main`
2. Check that Read the Docs builds automatically
3. Verify documentation is updated

## Step 6: Project Badges

Add badges to your README.md:

```markdown
[![CI](https://github.com/bryankemp/record-shelf/workflows/CI/badge.svg)](https://github.com/bryankemp/record-shelf/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/record-shelf.svg)](https://pypi.org/project/record-shelf/)
[![Documentation](https://readthedocs.org/projects/record-shelf/badge/?version=latest)](https://record-shelf.readthedocs.io/en/latest/)
[![codecov](https://codecov.io/gh/bryankemp/record-shelf/branch/main/graph/badge.svg)](https://codecov.io/gh/bryankemp/record-shelf)
```

## Step 7: Optional Enhancements

### 7.1 Code Coverage (Codecov)

1. Sign up at [Codecov](https://codecov.io/)
2. Connect your GitHub repository
3. Add `CODECOV_TOKEN` to GitHub secrets if private repo

### 7.2 Dependabot (Automated Dependencies)

Create `.github/dependabot.yml`:

```yaml
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
    reviewers:
      - "bryankemp"
```

### 7.3 Pre-commit Hooks

Create `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.1.0
    hooks:
      - id: black
  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort
  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
```

## Troubleshooting

### Common Issues

1. **PyPI Upload Fails**
   - Check API token is correct
   - Ensure version number hasn't been used
   - Verify package name is available

2. **Read the Docs Build Fails**
   - Check `docs/requirements.txt`
   - Verify `.readthedocs.yml` configuration
   - Review build logs for specific errors

3. **GitHub Actions Fail**
   - Check workflow syntax
   - Verify all secrets are set
   - Review action logs for details

### Getting Help

- GitHub Actions: [Documentation](https://docs.github.com/en/actions)
- PyPI: [Publishing Guide](https://packaging.python.org/tutorials/packaging-projects/)
- Read the Docs: [Documentation](https://docs.readthedocs.io/)

## Summary

Once set up, your workflow will be:

1. **Development**: Work on feature branches, create PRs
2. **CI**: Automated testing on every push/PR
3. **Release**: Tag releases to trigger automated PyPI publishing
4. **Documentation**: Automatic builds on Read the Docs
5. **Distribution**: Users can install via `pip install record-shelf`

Your project is now ready for professional development and distribution!

