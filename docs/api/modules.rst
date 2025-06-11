API Reference
=============

Record Shelf provides a well-structured API for developers who want to integrate
music collection reporting functionality into their own applications.

Core Modules
------------

.. toctree::
   :maxdepth: 2

   cli
   config
   report_generator
   utils

Quick Reference
---------------

Core Classes
~~~~~~~~~~~~

.. currentmodule:: record_shelf

.. autosummary::
   :toctree: _autosummary
   :template: class.rst

   Config
   ReportGenerator

Main Functions
~~~~~~~~~~~~~~

.. autosummary::
   :toctree: _autosummary
   :template: function.rst

   cli.main
   utils.setup_logging
   utils.print_stats

Usage Examples
--------------

Basic API Usage
~~~~~~~~~~~~~~~

.. code-block:: python

   from record_shelf import Config, ReportGenerator

   # Create configuration
   config = Config(token="your_discogs_token")

   # Initialize report generator
   generator = ReportGenerator(config)

   # Fetch collection data
   data = generator.fetch_collection_data("username")

   # Generate report
   generator.create_report(data, "output.xlsx", "xlsx")

Advanced Usage
~~~~~~~~~~~~~~

.. code-block:: python

   from record_shelf import Config, ReportGenerator
   from record_shelf.utils import setup_logging, print_stats

   # Setup logging
   setup_logging(debug=True)

   # Create configuration with custom settings
   config = Config(
       token="your_discogs_token",
       user_agent="MyApp/1.0",
       rate_limit_delay=2.0,
       debug=True
   )

   # Initialize report generator
   generator = ReportGenerator(config)

   # Get available shelves
   shelves = generator.get_user_shelves("username")
   print(f"Available shelves: {shelves}")

   # Fetch filtered data
   data = generator.fetch_collection_data(
       username="username",
       shelf_filter="Vinyl"
   )

   # Generate statistics
   stats = generator.generate_summary_stats(data)
   print_stats(stats)

   # Create multiple format reports
   generator.create_report(data, "vinyl.xlsx", "xlsx")
   generator.create_report(data, "vinyl.csv", "csv")
   generator.create_report(data, "vinyl.html", "html")

Type Hints
----------

Record Shelf includes comprehensive type hints for better IDE support and code quality:

.. code-block:: python

   from typing import Dict, List, Any, Optional
   from record_shelf import Config, ReportGenerator

   def process_collection(
       username: str,
       token: str,
       shelf_filter: Optional[str] = None
   ) -> List[Dict[str, Any]]:
       config = Config(token=token)
       generator = ReportGenerator(config)
       return generator.fetch_collection_data(username, shelf_filter)

Error Handling
--------------

.. code-block:: python

   from record_shelf import Config, ReportGenerator
   import logging

   try:
       config = Config(token="invalid_token")
       generator = ReportGenerator(config)
       data = generator.fetch_collection_data("username")
   except ValueError as e:
       logging.error(f"Configuration error: {e}")
   except Exception as e:
       logging.error(f"API error: {e}")

Customization
-------------

Custom Configuration
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from record_shelf import Config

   # Custom configuration
   config = Config(
       token="your_token",
       user_agent="CustomApp/2.0",
       rate_limit_delay=0.5,  # Faster requests (be careful!)
       debug=True
   )

Custom Processing
~~~~~~~~~~~~~~~~~

.. code-block:: python

   from record_shelf import ReportGenerator
   import pandas as pd

   # Custom data processing
   def process_vinyl_only(data):
       df = pd.DataFrame(data)
       vinyl_only = df[df['format'].str.contains('Vinyl', na=False)]
       return vinyl_only.to_dict('records')

   # Use with generator
   generator = ReportGenerator(config)
   raw_data = generator.fetch_collection_data("username")
   vinyl_data = process_vinyl_only(raw_data)
   generator.create_report(vinyl_data, "vinyl_only.xlsx")

Extending Functionality
-----------------------

Custom Report Generator
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from record_shelf import ReportGenerator, Config
   import pandas as pd

   class CustomReportGenerator(ReportGenerator):
       def create_summary_report(self, data, output_path):
           """Create a summary report with statistics."""
           df = pd.DataFrame(data)
           
           summary = {
               'total_items': len(df),
               'unique_artists': df['artist'].nunique(),
               'formats': df['format'].value_counts().to_dict(),
               'years': df['year'].value_counts().sort_index().to_dict()
           }
           
           # Create summary DataFrame
           summary_df = pd.DataFrame([
               {'Metric': k, 'Value': v} for k, v in summary.items()
               if not isinstance(v, dict)
           ])
           
           with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
               summary_df.to_excel(writer, sheet_name='Summary', index=False)
               df.to_excel(writer, sheet_name='Full Data', index=False)

   # Usage
   config = Config(token="your_token")
   generator = CustomReportGenerator(config)
   data = generator.fetch_collection_data("username")
   generator.create_summary_report(data, "summary.xlsx")

Integration Examples
--------------------

Flask Web Application
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from flask import Flask, request, send_file
   from record_shelf import Config, ReportGenerator
   import tempfile
   import os

   app = Flask(__name__)

   @app.route('/generate_report', methods=['POST'])
   def generate_report():
       username = request.form['username']
       token = request.form['token']
       format_type = request.form.get('format', 'xlsx')
       
       try:
           config = Config(token=token)
           generator = ReportGenerator(config)
           data = generator.fetch_collection_data(username)
           
           # Create temporary file
           with tempfile.NamedTemporaryFile(delete=False, suffix=f'.{format_type}') as tmp:
               generator.create_report(data, tmp.name, format_type)
               return send_file(tmp.name, as_attachment=True, 
                              download_name=f'{username}_collection.{format_type}')
       except Exception as e:
           return f"Error: {e}", 400

CLI Integration
~~~~~~~~~~~~~~~

.. code-block:: python

   import click
   from record_shelf import Config, ReportGenerator

   @click.command()
   @click.option('--username', required=True)
   @click.option('--token', envvar='DISCOGS_TOKEN')
   @click.option('--output', default='report.xlsx')
   def my_custom_command(username, token, output):
       """Custom command using Record Shelf API."""
       config = Config(token=token)
       generator = ReportGenerator(config)
       
       click.echo(f"Fetching data for {username}...")
       data = generator.fetch_collection_data(username)
       
       click.echo(f"Generating report to {output}...")
       generator.create_report(data, output)
       
       click.echo("Done!")

   if __name__ == '__main__':
       my_custom_command()

