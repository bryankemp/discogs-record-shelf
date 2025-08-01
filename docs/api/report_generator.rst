Report Generator Module
========================

.. automodule:: record_shelf.report_generator
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

Report Generation
-----------------

The ReportGenerator class is the core component for generating collection reports
from Discogs data.

ReportGenerator Class
~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: record_shelf.report_generator.ReportGenerator
   :members:
   :undoc-members:
   :show-inheritance:

Usage Examples
--------------

Basic Report Generation
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from record_shelf import Config, ReportGenerator

   # Create configuration
   config = Config(token="your_discogs_token")

   # Initialize report generator
   generator = ReportGenerator(config)

   # Fetch collection data
   data = generator.fetch_collection_data("username")

   # Generate Excel report
   generator.create_report(data, "collection.xlsx", "xlsx")

Filtered Report Generation
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from record_shelf import Config, ReportGenerator

   config = Config(token="your_token")
   generator = ReportGenerator(config)

   # Get available categories
   categories = generator.get_user_categories("username")
   print(f"Available categories: {categories}")

   # Generate filtered report
   vinyl_data = generator.fetch_collection_data(
       username="username",
       category_filter="Vinyl"
   )

   generator.create_report(vinyl_data, "vinyl.xlsx", "xlsx")

Multiple Format Generation
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from record_shelf import Config, ReportGenerator

   config = Config(token="your_token")
   generator = ReportGenerator(config)

   # Fetch data once
   data = generator.fetch_collection_data("username")

   # Generate multiple formats
   generator.create_report(data, "collection.xlsx", "xlsx")
   generator.create_report(data, "collection.csv", "csv")
   generator.create_report(data, "collection.html", "html")

Statistics Generation
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from record_shelf import Config, ReportGenerator
   from record_shelf.utils import print_stats

   config = Config(token="your_token")
   generator = ReportGenerator(config)

   data = generator.fetch_collection_data("username")
   stats = generator.generate_summary_stats(data)
   
   print_stats(stats)

Method Documentation
--------------------

Data Fetching Methods
~~~~~~~~~~~~~~~~~~~~~

.. automethod:: record_shelf.report_generator.ReportGenerator.fetch_collection_data

.. automethod:: record_shelf.report_generator.ReportGenerator.get_user_categories

Report Creation Methods
~~~~~~~~~~~~~~~~~~~~~~~

.. automethod:: record_shelf.report_generator.ReportGenerator.create_report

.. automethod:: record_shelf.report_generator.ReportGenerator.generate_summary_stats

Data Processing
---------------

The ReportGenerator processes Discogs data through several stages:

1. **API Interaction**: Connects to Discogs API using provided credentials
2. **Data Extraction**: Retrieves collection data with rate limiting
3. **Data Processing**: Cleans and organizes the raw data
4. **Sorting**: Orders data by shelf, artist, and title
5. **Report Generation**: Creates formatted output files

Data Fields
~~~~~~~~~~~

The following fields are extracted from each release:

- **Basic Information**: shelf, artist, title, label, catalog_number
- **Format Details**: format, year, country
- **Classification**: genre, style
- **Identifiers**: discogs_id, master_id
- **Personal Data**: rating, notes

Error Handling
~~~~~~~~~~~~~~

The ReportGenerator includes comprehensive error handling:

- **API Errors**: Rate limiting, authentication, network issues
- **Data Errors**: Missing or malformed release data
- **File Errors**: Permissions, disk space, format issues

Rate Limiting
~~~~~~~~~~~~~

Built-in rate limiting ensures respectful API usage:

- Default 1 second delay between requests
- Configurable delay settings
- Progress indicators for long operations
- Automatic retry on temporary failures

Best Practices
--------------

Performance
~~~~~~~~~~~

- Use shelf filtering for large collections
- Generate CSV format for faster processing
- Process during off-peak hours
- Monitor memory usage for very large collections

Reliability
~~~~~~~~~~~

- Always handle exceptions in your code
- Validate data before processing
- Use debug logging for troubleshooting
- Implement retry logic for network issues

Security
~~~~~~~~

- Store API tokens securely
- Use environment variables for configuration
- Validate user inputs
- Monitor API usage

Extensibility
~~~~~~~~~~~~~

The ReportGenerator can be extended for custom functionality:

.. code-block:: python

   class CustomReportGenerator(ReportGenerator):
       def create_vinyl_only_report(self, username, output_path):
           """Generate a report with only vinyl releases."""
           data = self.fetch_collection_data(username)
           vinyl_data = [item for item in data if 'vinyl' in item['format'].lower()]
           self.create_report(vinyl_data, output_path, 'xlsx')

