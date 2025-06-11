Usage Guide
===========

Command Line Interface
----------------------

Record Shelf provides a command-line interface with two main commands:

- ``generate`` - Generate collection reports
- ``list-shelves`` - List available shelves

Basic Syntax
~~~~~~~~~~~~

::

    record-shelf [GLOBAL_OPTIONS] COMMAND [COMMAND_OPTIONS]

Global Options
~~~~~~~~~~~~~~

``--debug``
   Enable debug logging for troubleshooting

``--help``
   Show help message and exit

Generate Command
----------------

The ``generate`` command creates collection reports with various customization options.

Syntax
~~~~~~

::

    record-shelf generate [OPTIONS]

Required Options
~~~~~~~~~~~~~~~~

``--username TEXT``
   Discogs username (required)

Optional Arguments
~~~~~~~~~~~~~~~~~~

``--token TEXT``
   Discogs API token. If not provided, uses the ``DISCOGS_TOKEN`` environment variable.

``--output TEXT, -o TEXT``
   Output file path (default: ``collection_report.xlsx``)

``--shelf TEXT``
   Filter by specific shelf name (optional). If not specified, includes all shelves.

``--format [xlsx|csv|html]``
   Output format (default: ``xlsx``)

Examples
~~~~~~~~

**Basic usage**::

    record-shelf generate --username myusername

**With custom output file**::

    record-shelf generate --username myusername --output my_collection.xlsx

**Filter by shelf**::

    record-shelf generate --username myusername --shelf "Vinyl"

**CSV format**::

    record-shelf generate --username myusername --format csv --output collection.csv

**HTML format**::

    record-shelf generate --username myusername --format html --output collection.html

**With API token**::

    record-shelf generate --token abc123def456 --username myusername

**Debug mode**::

    record-shelf --debug generate --username myusername

List Shelves Command
--------------------

The ``list-shelves`` command displays all available shelves in a user's collection.

Syntax
~~~~~~

::

    record-shelf list-shelves [OPTIONS]

Required Options
~~~~~~~~~~~~~~~~

``--username TEXT``
   Discogs username (required)

Optional Arguments
~~~~~~~~~~~~~~~~~~

``--token TEXT``
   Discogs API token. If not provided, uses the ``DISCOGS_TOKEN`` environment variable.

Examples
~~~~~~~~

**Basic usage**::

    record-shelf list-shelves --username myusername

**With API token**::

    record-shelf list-shelves --token abc123def456 --username myusername

Output Formats
--------------

Record Shelf supports three output formats:

Excel (.xlsx)
~~~~~~~~~~~~~

- **Default format**
- **Main features**:
  - "Collection" sheet with all items
  - Separate sheet for each shelf
  - Professional formatting
  - Sortable columns
  - Excel-compatible formulas

**Best for**: Detailed analysis, sharing with others, professional reports

CSV (.csv)
~~~~~~~~~~

- **Plain text format**
- **Main features**:
  - Single file with all data
  - Compatible with spreadsheet applications
  - Easy to import into databases
  - Universal format support

**Best for**: Data analysis, importing to other tools, automation

HTML (.html)
~~~~~~~~~~~~

- **Web format**
- **Main features**:
  - Viewable in any web browser
  - Professional table styling
  - No additional software required
  - Easy to share via web

**Best for**: Web viewing, sharing online, quick previews

Data Fields
-----------

All reports include the following data fields:

**Core Information**

- **Shelf**: Collection folder/shelf name
- **Artist**: Artist name(s)
- **Title**: Release title
- **Label**: Record label(s)
- **Catalog Number**: Label catalog number(s)

**Format Details**

- **Format**: Format details (e.g., "Vinyl, LP, Album")
- **Year**: Release year
- **Country**: Country of release

**Classification**

- **Genre**: Music genre(s)
- **Style**: Music style(s)

**Identifiers**

- **Discogs ID**: Unique Discogs release ID
- **Master ID**: Master release ID (if applicable)

**Personal Data**

- **Rating**: Your rating (if set)
- **Notes**: Your personal notes (if any)

Sorting and Organization
------------------------

Record Shelf automatically sorts data in a logical hierarchy:

1. **Primary sort**: By shelf name (alphabetical)
2. **Secondary sort**: By artist name (alphabetical, case-insensitive)
3. **Tertiary sort**: By title (alphabetical, case-insensitive)

This ensures consistent, predictable organization across all reports.

Rate Limiting
-------------

Record Shelf includes built-in rate limiting to respect Discogs API limits:

- **Default delay**: 1 second between API calls
- **Progress indicators**: Visual progress bars for long operations
- **Automatic retry**: Built-in retry logic for rate limit errors
- **Respectful usage**: Designed to stay within API limits

Error Handling
--------------

Record Shelf provides comprehensive error handling:

**Authentication Errors**

- Clear messages for invalid tokens
- Guidance on obtaining tokens
- Environment variable instructions

**API Errors**

- Rate limiting detection
- Network error handling
- Service unavailability alerts

**Data Errors**

- Graceful handling of missing data
- Partial data recovery
- Detailed error logging

**File Errors**

- Permission error detection
- Disk space warnings
- File format validation

Logging
-------

Record Shelf provides detailed logging:

**Log Levels**

- **INFO**: Normal operation messages
- **DEBUG**: Detailed operation information (use ``--debug``)
- **WARNING**: Non-fatal issues
- **ERROR**: Fatal errors

**Log Destinations**

- **Console**: Real-time feedback
- **File**: ``record_shelf.log`` in current directory

**Log Content**

- API call details
- Processing progress
- Error diagnostics
- Performance metrics

Advanced Usage
--------------

Automation Scripts
~~~~~~~~~~~~~~~~~~

Record Shelf is designed for automation::

    #!/bin/bash
    # Backup script
    export DISCOGS_TOKEN="your_token"
    
    # Generate daily backup
    record-shelf generate --username myuser --output "backup_$(date +%Y%m%d).xlsx"
    
    # Generate format-specific reports
    record-shelf generate --username myuser --shelf "Vinyl" --output vinyl.csv --format csv
    record-shelf generate --username myuser --shelf "CD" --output cd.html --format html

Batch Processing
~~~~~~~~~~~~~~~~

Process multiple users or shelves::

    #!/bin/bash
    export DISCOGS_TOKEN="your_token"
    
    for shelf in "Vinyl" "CD" "Digital"; do
        record-shelf generate --username myuser --shelf "$shelf" --output "${shelf,,}.xlsx"
    done

Cron Jobs
~~~~~~~~~

Schedule regular reports::

    # Run daily at 2 AM
    0 2 * * * /path/to/record-shelf generate --username myuser --output /backup/daily.xlsx
    
    # Run weekly full report
    0 0 * * 0 /path/to/record-shelf generate --username myuser --output /backup/weekly.xlsx

Troubleshooting
---------------

Common Issues and Solutions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**"No module named 'record_shelf'"**
   - Ensure Record Shelf is installed: ``pip install record-shelf``
   - Check if you're in the correct virtual environment

**"Authentication failed"**
   - Verify your Discogs token is correct
   - Check the ``DISCOGS_TOKEN`` environment variable
   - Ensure token has proper permissions

**"User not found"**
   - Verify the username is correct
   - Check if the user's collection is public

**"Rate limit exceeded"**
   - Wait a few minutes and try again
   - Record Shelf includes automatic rate limiting

**"Permission denied" when writing files**
   - Check file permissions in the output directory
   - Ensure you have write access to the target location

**"Empty collection"**
   - Verify the user has items in their collection
   - Check if you're filtering by a non-existent shelf

Performance Tips
~~~~~~~~~~~~~~~~

**Large Collections**
   - Use shelf filtering to process smaller subsets
   - Run during off-peak hours
   - Consider CSV format for faster processing

**Slow Network**
   - Increase rate limiting delay (requires code modification)
   - Use debug mode to monitor progress
   - Process during better network conditions

**Memory Usage**
   - CSV format uses less memory than Excel
   - Process shelves separately for very large collections
   - Close other applications during processing

