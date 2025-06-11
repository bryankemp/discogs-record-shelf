Configuration
=============

Record Shelf provides several configuration options to customize its behavior.

API Token Setup
---------------

Before using Record Shelf, you need to obtain a Discogs API token:

1. **Visit Discogs Developer Settings**
   
   Go to https://www.discogs.com/settings/developers

2. **Create or Select Application**
   
   - Create a new application or use an existing one
   - Fill in the required information
   - Note your Consumer Key and Consumer Secret

3. **Generate Personal Access Token**
   
   - Click "Generate new token"
   - Copy the generated token
   - Store it securely

Token Configuration
-------------------

Environment Variable (Recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set the token as an environment variable::

    # Linux/Mac
    export DISCOGS_TOKEN="your_token_here"
    
    # Windows Command Prompt
    set DISCOGS_TOKEN=your_token_here
    
    # Windows PowerShell
    $env:DISCOGS_TOKEN="your_token_here"

Command Line Option
~~~~~~~~~~~~~~~~~~~

Pass the token directly to commands::

    record-shelf --token "your_token_here" generate --username myuser

Configuration File
~~~~~~~~~~~~~~~~~~

Create a ``.env`` file in your project directory::

    DISCOGS_TOKEN=your_token_here

Advanced Configuration
----------------------

Rate Limiting
~~~~~~~~~~~~~

Record Shelf includes built-in rate limiting to respect Discogs API limits:

- **Default delay**: 1 second between API calls
- **Configurable**: Can be adjusted via code configuration
- **Automatic**: No manual intervention required

To modify rate limiting in code::

    from record_shelf import Config
    
    config = Config(
        token="your_token",
        rate_limit_delay=2.0  # 2 seconds between requests
    )

User Agent
~~~~~~~~~~

Customize the User-Agent header for API requests::

    from record_shelf import Config
    
    config = Config(
        token="your_token",
        user_agent="MyApp/1.0"
    )

Logging Configuration
~~~~~~~~~~~~~~~~~~~~~

Record Shelf provides detailed logging:

**Log Levels**:

- ``INFO``: Standard operation messages
- ``DEBUG``: Detailed debugging information
- ``WARNING``: Non-fatal issues
- ``ERROR``: Fatal errors

**Enable Debug Logging**::

    record-shelf --debug generate --username myuser

**Log File Location**:

- Default: ``record_shelf.log`` in current directory
- Contains detailed operation logs
- Rotated automatically

Output Configuration
--------------------

File Formats
~~~~~~~~~~~~

Record Shelf supports multiple output formats:

.. list-table:: Supported Formats
   :widths: 15 25 60
   :header-rows: 1

   * - Format
     - Extension
     - Description
   * - Excel
     - ``.xlsx``
     - Default format with multiple sheets
   * - CSV
     - ``.csv``
     - Comma-separated values
   * - HTML
     - ``.html``
     - Web-viewable table

Default Settings
~~~~~~~~~~~~~~~~

- **Default output file**: ``collection_report.xlsx``
- **Default format**: Excel (``.xlsx``)
- **Default location**: Current working directory

Custom Output::

    record-shelf generate --username myuser --output my_collection.csv --format csv

Filtering Configuration
-----------------------

Shelf Filtering
~~~~~~~~~~~~~~~

Filter reports by specific shelves::

    # Single shelf
    record-shelf generate --username myuser --shelf "Vinyl"
    
    # List available shelves first
    record-shelf list-shelves --username myuser

Data Filtering
~~~~~~~~~~~~~~

Record Shelf automatically filters and organizes data:

- **Sorting**: By shelf, then artist, then title
- **Deduplication**: Removes duplicate entries
- **Cleaning**: Handles missing or invalid data gracefully

Security Configuration
----------------------

Token Security
~~~~~~~~~~~~~~

**Best Practices**:

- Store tokens in environment variables
- Never commit tokens to version control
- Use different tokens for different environments
- Rotate tokens periodically
- Limit token permissions if possible

**Token Storage**::

    # Good: Environment variable
    export DISCOGS_TOKEN="token_here"
    
    # Bad: Hardcoded in script
    config = Config(token="token_here")  # Don't do this!

Network Security
~~~~~~~~~~~~~~~~

- All API calls use HTTPS
- No sensitive data stored locally
- Rate limiting prevents abuse
- Respectful API usage

Performance Configuration
-------------------------

Optimization Settings
~~~~~~~~~~~~~~~~~~~~~

**For Large Collections**:

- Use shelf filtering to process smaller subsets
- Increase rate limiting delay for stability
- Use CSV format for faster processing
- Run during off-peak hours

**For Slow Networks**:

- Increase rate limiting delay
- Enable debug mode to monitor progress
- Process during better network conditions

**Memory Optimization**:

- CSV format uses less memory than Excel
- Process shelves separately for very large collections
- Close other applications during processing

Troubleshooting Configuration
-----------------------------

Common Configuration Issues
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Token Not Found**::

    Error: Discogs API token is required
    
    Solution:
    - Set DISCOGS_TOKEN environment variable
    - Or use --token command line option

**Invalid Token**::

    Error: Authentication failed
    
    Solution:
    - Verify token is correct
    - Check token hasn't expired
    - Ensure token has proper permissions

**Permission Errors**::

    Error: Permission denied writing to file
    
    Solution:
    - Check file permissions
    - Ensure write access to output directory
    - Try different output location

Configuration Validation
~~~~~~~~~~~~~~~~~~~~~~~~~

Test your configuration::

    # Test basic connectivity
    record-shelf list-shelves --username your_username
    
    # Test with debug logging
    record-shelf --debug list-shelves --username your_username
    
    # Test output formats
    record-shelf generate --username your_username --format csv --output test.csv

Development Configuration
-------------------------

Development Environment
~~~~~~~~~~~~~~~~~~~~~~~

For development and testing::

    # Clone repository
    git clone https://github.com/username/record-shelf.git
    cd record-shelf
    
    # Setup development environment
    make setup
    
    # Activate virtual environment
    source venv/bin/activate
    
    # Install in development mode
    pip install -e ".[dev]"

Testing Configuration
~~~~~~~~~~~~~~~~~~~~~

Test environment setup::

    # Run tests
    pytest
    
    # Run with coverage
    pytest --cov=record_shelf
    
    # Run linting
    make lint
    
    # Run all checks
    make dev-test

