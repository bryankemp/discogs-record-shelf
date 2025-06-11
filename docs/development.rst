Development
===========

This section covers development setup, contribution guidelines, and technical details for contributors.

Development Environment
-----------------------

Setting up a development environment for record-shelf:

.. code-block:: bash

   # Clone the repository
   git clone https://github.com/bryankemp/record-shelf.git
   cd record-shelf

   # Set up development environment
   make setup
   source venv/bin/activate  # On Windows: venv\Scripts\activate

   # Install pre-commit hooks
   make pre-commit

Development Commands
--------------------

The project includes several make targets for development:

**Testing**

.. code-block:: bash

   make test          # Run all tests
   make test-cov      # Run tests with coverage
   make qtest         # Quick test run

**Code Quality**

.. code-block:: bash

   make lint          # Run all linting tools
   make format        # Format code with black and isort
   make type-check    # Run mypy type checking
   make security      # Run security checks
   make dev-test      # Run all development checks

**Documentation**

.. code-block:: bash

   make docs          # Build documentation
   make docs-serve    # Serve documentation locally
   make docs-rebuild  # Clean and rebuild docs

**Building and Publishing**

.. code-block:: bash

   make build         # Build package
   make clean         # Clean build artifacts
   make upload        # Upload to PyPI (maintainers only)

Code Standards
--------------

The project follows these coding standards:

- **PEP 8** style guidelines
- **Black** for code formatting (88 character line length)
- **isort** for import sorting
- **mypy** for type checking
- **pylint** for additional linting
- **Google-style** docstrings
- **Type hints** for all functions and methods

Testing Guidelines
------------------

- Write tests for all new features and bug fixes
- Maintain or improve test coverage (currently >90%)
- Use pytest for testing framework
- Mock external API calls in tests
- Include both unit and integration tests

Project Structure
-----------------

.. code-block:: text

   record_shelf/
   ├── record_shelf/          # Main package
   │   ├── __init__.py
   │   ├── cli.py            # Command-line interface
   │   ├── config.py         # Configuration management
   │   ├── report_generator.py  # Core report generation
   │   └── utils.py          # Utility functions
   ├── tests/                # Test suite
   ├── docs/                 # Documentation
   ├── .github/              # GitHub workflows
   ├── pyproject.toml        # Project configuration
   ├── Makefile             # Development commands
   └── README.md            # Project overview

Release Process
---------------

The project uses automated releases via GitHub Actions:

1. Update version in ``pyproject.toml``
2. Update ``CHANGELOG.md``
3. Create and push a git tag: ``git tag v1.0.0 && git push origin v1.0.0``
4. GitHub Actions will automatically:
   - Run tests
   - Build the package
   - Publish to PyPI
   - Create a GitHub release

Continuous Integration
----------------------

The project uses GitHub Actions for CI/CD:

- **CI Pipeline**: Runs on every push and pull request
  - Tests across Python 3.8-3.11 and multiple OS (Ubuntu, Windows, macOS)
  - Code quality checks (linting, formatting, type checking)
  - Security scanning
  - Documentation building

- **Release Pipeline**: Runs on git tags
  - Full test suite
  - Package building and validation
  - PyPI publishing
  - GitHub release creation

For more detailed contribution guidelines, see the `CONTRIBUTING.md <https://github.com/bryankemp/record-shelf/blob/main/CONTRIBUTING.md>`_ file.

