Utils Module
============

.. automodule:: record_shelf.utils
   :members:
   :undoc-members:
   :show-inheritance:

Utility Functions
-----------------

The utils module provides utility functions for logging, statistics display,
and data validation.

Logging Functions
~~~~~~~~~~~~~~~~~

.. autofunction:: record_shelf.utils.setup_logging

Statistics Functions
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: record_shelf.utils.print_stats

Validation Functions
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: record_shelf.utils.validate_username

.. autofunction:: record_shelf.utils.sanitize_filename

Usage Examples
--------------

Logging Setup
~~~~~~~~~~~~~

.. code-block:: python

   from record_shelf.utils import setup_logging

   # Setup basic logging
   setup_logging()

   # Setup debug logging
   setup_logging(debug=True)

Statistics Display
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from record_shelf import Config, ReportGenerator
   from record_shelf.utils import print_stats

   config = Config(token="your_token")
   generator = ReportGenerator(config)

   data = generator.fetch_collection_data("username")
   stats = generator.generate_summary_stats(data)
   
   # Print formatted statistics
   print_stats(stats)

Data Validation
~~~~~~~~~~~~~~~

.. code-block:: python

   from record_shelf.utils import validate_username, sanitize_filename

   # Validate username format
   username = "my_username"
   if validate_username(username):
       print(f"{username} is valid")
   else:
       print(f"{username} is invalid")

   # Sanitize filename
   unsafe_name = "my/file<name>?.xlsx"
   safe_name = sanitize_filename(unsafe_name)
   print(f"Safe filename: {safe_name}")

Advanced Usage
--------------

Custom Logging Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import logging
   from record_shelf.utils import setup_logging

   # Setup logging with custom configuration
   setup_logging(debug=True)
   
   # Get logger for custom use
   logger = logging.getLogger('record_shelf')
   logger.info("Custom log message")

Statistics Processing
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from record_shelf import Config, ReportGenerator
   from record_shelf.utils import print_stats

   config = Config(token="your_token")
   generator = ReportGenerator(config)

   data = generator.fetch_collection_data("username")
   stats = generator.generate_summary_stats(data)
   
   # Custom statistics processing
   print(f"Total items: {stats['total_items']}")
   print(f"Shelves: {', '.join(stats['shelves'])}")
   
   # Top artists
   for artist, count in list(stats['top_artists'].items())[:5]:
       print(f"{artist}: {count} releases")

Function Documentation
----------------------

Logging Functions
~~~~~~~~~~~~~~~~~

**setup_logging(debug=False)**

Configures logging for the application.

:param debug: Enable debug-level logging
:type debug: bool
:returns: None

**Features**:

- Console and file logging
- Configurable log levels
- Automatic log file creation
- Thread-safe logging

**Log Levels**:

- ``INFO``: General information messages
- ``DEBUG``: Detailed debugging information
- ``WARNING``: Warning messages for non-fatal issues
- ``ERROR``: Error messages for fatal issues

**Log Files**:

- Default location: ``record_shelf.log`` in current directory
- Automatic rotation when files get large
- UTF-8 encoding for international characters

Statistics Functions
~~~~~~~~~~~~~~~~~~~~

**print_stats(stats)**

Prints collection statistics in a readable format.

:param stats: Statistics dictionary from ReportGenerator
:type stats: Dict[str, Any]
:returns: None

**Output Format**:

- Total item count
- Items per shelf breakdown
- Top 10 artists by release count
- Format distribution
- Clean, readable formatting

Validation Functions
~~~~~~~~~~~~~~~~~~~~

**validate_username(username)**

Validates Discogs username format.

:param username: Username to validate
:type username: str
:returns: True if valid, False otherwise
:rtype: bool

**Validation Rules**:

- Must not be empty
- Can contain letters, numbers, underscores, hyphens
- No spaces or special characters
- Case-insensitive

**sanitize_filename(filename)**

Sanitizes filenames for cross-platform compatibility.

:param filename: Original filename
:type filename: str
:returns: Sanitized filename
:rtype: str

**Sanitization Rules**:

- Removes or replaces problematic characters
- Ensures compatibility across operating systems
- Preserves file extensions
- Trims whitespace

Best Practices
--------------

Logging
~~~~~~~

- Always call ``setup_logging()`` at application start
- Use debug logging for development and troubleshooting
- Check log files for error patterns
- Rotate log files regularly in production

Statistics
~~~~~~~~~~

- Generate statistics after data collection
- Use statistics to verify data quality
- Share statistics with users for transparency
- Store statistics for historical analysis

Validation
~~~~~~~~~~

- Validate all user inputs
- Sanitize filenames before file operations
- Check return values from validation functions
- Provide clear error messages for invalid inputs

Error Handling
--------------

The utils module includes error handling for common issues:

**Logging Errors**:

- File permission issues
- Disk space problems
- Invalid log levels

**Statistics Errors**:

- Empty or invalid data
- Missing required fields
- Type conversion errors

**Validation Errors**:

- Invalid input types
- Empty or None values
- Encoding issues

Integration Examples
--------------------

Complete Application Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from record_shelf import Config, ReportGenerator
   from record_shelf.utils import setup_logging, validate_username, sanitize_filename
   import sys

   def main():
       # Setup logging
       setup_logging(debug=True)
       
       # Validate inputs
       username = input("Enter Discogs username: ")
       if not validate_username(username):
           print("Invalid username format")
           sys.exit(1)
       
       # Sanitize output filename
       raw_filename = f"{username}_collection.xlsx"
       filename = sanitize_filename(raw_filename)
       
       # Generate report
       config = Config(token="your_token")
       generator = ReportGenerator(config)
       
       data = generator.fetch_collection_data(username)
       generator.create_report(data, filename, "xlsx")
       
       print(f"Report saved as: {filename}")

   if __name__ == "__main__":
       main()

Custom Statistics Display
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from record_shelf.utils import print_stats
   import json

   def save_stats_to_file(stats, filename):
       """Save statistics to JSON file."""
       with open(filename, 'w') as f:
           json.dump(stats, f, indent=2)

   def custom_stats_display(stats):
       """Custom statistics display."""
       print("=== COLLECTION SUMMARY ===")
       print(f"📊 Total Releases: {stats['total_items']}")
       print(f"📂 Shelves: {len(stats['shelves'])}")
       
       if 'top_artists' in stats:
           print("\n🎵 Top Artists:")
           for i, (artist, count) in enumerate(stats['top_artists'].items(), 1):
               print(f"  {i}. {artist} ({count} releases)")
               if i >= 5:  # Show only top 5
                   break

   # Usage
   stats = generator.generate_summary_stats(data)
   custom_stats_display(stats)
   save_stats_to_file(stats, "collection_stats.json")

