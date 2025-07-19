Discogs Record Shelf Documentation
====================================

.. image:: https://img.shields.io/pypi/v/discogs-record-shelf
   :target: https://pypi.org/project/discogs-record-shelf/
   :alt: PyPI Version

.. image:: https://img.shields.io/badge/python-3.8+-blue.svg
   :target: https://www.python.org/downloads/
   :alt: Python 3.8+

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: black

.. image:: https://img.shields.io/badge/License-BSD%203--Clause-blue.svg
   :target: https://opensource.org/licenses/BSD-3-Clause
   :alt: License: BSD 3-Clause

Discogs Record Shelf is a professional Python tool for creating custom reports from your Discogs music collection with intelligent sorting by shelf and alphabetical organization.

Features
--------

📊 **Multiple Output Formats**
   Generate detailed collection reports in Excel, CSV, or HTML format

🗂️ **Smart Organization**
   Sort items by shelf, then alphabetically by artist and title

🔍 **Flexible Filtering**
   Filter reports by specific shelves or generate complete collection reports

📑 **Excel Integration**
   Export separate sheets for each shelf with professional formatting

🖥️ **Command-Line Interface**
   Easy-to-use CLI for automation and scripting

⏱️ **API Rate Limiting**
   Built-in rate limiting to respect Discogs API limits

📝 **Comprehensive Logging**
   Detailed logging and error handling for troubleshooting

🧪 **Full Test Coverage**
   Comprehensive test suite with pytest

🔧 **Professional Development**
   Complete development setup with tox, pylint, and black

Quick Start
-----------

1. **Installation**::

    pip install discogs-record-shelf

2. **Get your Discogs API token** from https://www.discogs.com/settings/developers

3. **Set your token**::

    export DISCOGS_TOKEN="your_token_here"

4. **Generate a report**::

    record-shelf generate --username YOUR_DISCOGS_USERNAME

5. **List available shelves**::

    record-shelf list-shelves --username YOUR_DISCOGS_USERNAME

Documentation Contents
----------------------

.. toctree::
   :maxdepth: 2
   :caption: User Guide:

   installation
   quickstart
   usage
   configuration
   output_formats

.. toctree::
   :maxdepth: 2
   :caption: API Reference:

   api/modules
   api/cli
   api/config
   api/report_generator
   api/utils

.. toctree::
   :maxdepth: 2
   :caption: Development:

   development
   contributing
   changelog

Examples
--------

**Generate a complete collection report**::

    record-shelf generate --username myusername --output my_collection.xlsx

**Filter by specific shelf**::

    record-shelf generate --username myusername --shelf "Vinyl" --output vinyl_only.csv --format csv

**Generate HTML report with debug logging**::

    record-shelf --debug generate --username myusername --format html --output collection.html

Support
-------

- **Documentation**: You're reading it!
- **Issues**: Report bugs and feature requests on GitHub
- **Email**: bryan@kempville.com

License
-------

This project is licensed under the BSD 3-Clause License - see the LICENSE file for details.

Please respect Discogs' Terms of Service and API rate limits when using this tool.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
