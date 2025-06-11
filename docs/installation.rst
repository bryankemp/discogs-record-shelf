Installation
============

System Requirements
-------------------

- Python 3.8 or higher
- pip (Python package installer)
- Internet connection for Discogs API access

Installation Options
--------------------

From PyPI (Recommended)
~~~~~~~~~~~~~~~~~~~~~~~

Install the latest stable release from PyPI::

    pip install record-shelf

From Source
~~~~~~~~~~~

Clone the repository and install in development mode::

    git clone https://github.com/username/record-shelf.git
    cd record-shelf
    pip install -e ".[dev]"

Development Installation
~~~~~~~~~~~~~~~~~~~~~~~~

For development with all tools::

    git clone https://github.com/username/record-shelf.git
    cd record-shelf
    make setup

Verification
------------

Verify the installation by checking the version::

    record-shelf --help

You should see the help message with available commands.

Dependencies
------------

Record Shelf requires the following Python packages:

- **requests**: HTTP library for API calls
- **pandas**: Data manipulation and analysis
- **openpyxl**: Excel file support
- **discogs-client**: Discogs API client
- **click**: Command-line interface framework
- **tqdm**: Progress bars

Development dependencies include:

- **pytest**: Testing framework
- **pytest-cov**: Coverage testing
- **pylint**: Code analysis
- **black**: Code formatting
- **isort**: Import sorting
- **mypy**: Type checking
- **tox**: Testing automation
- **sphinx**: Documentation generation

Troubleshooting
---------------

Common Installation Issues
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Permission denied errors**::

    pip install --user record-shelf

**Python version conflicts**::

    python3 -m pip install record-shelf

**Virtual environment recommended**::

    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install record-shelf

Next Steps
----------

After installation, see the :doc:`quickstart` guide to begin using Record Shelf.

