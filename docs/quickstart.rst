Quick Start Guide
==================

This guide will help you get started with Record Shelf in just a few minutes.

Step 1: Get Your Discogs API Token
-----------------------------------

Before using Record Shelf, you need a Discogs API token:

1. Go to `Discogs Developer Settings <https://www.discogs.com/settings/developers>`_
2. Create a new application or use an existing one
3. Generate a personal access token
4. Copy your token for use with Record Shelf

.. warning::
   Keep your API token secure! Don't share it publicly or commit it to version control.

Step 2: Set Up Your Token
--------------------------

You can provide your token in two ways:

**Option 1: Environment Variable (Recommended)**::

    export DISCOGS_TOKEN="your_token_here"

**Option 2: Command Line Flag**::

    record-shelf --token "your_token_here" [command]

Step 3: Your First Report
-------------------------

Generate a complete collection report::

    record-shelf generate --username YOUR_DISCOGS_USERNAME

This will create a file called ``collection_report.xlsx`` with your entire collection.

Step 4: Explore Your Collection
-------------------------------

List available shelves in your collection::

    record-shelf list-shelves --username YOUR_DISCOGS_USERNAME

Example output::

    Available shelves:
      - All
      - Vinyl
      - CD
      - Digital
      - Wishlist

Step 5: Customize Your Reports
------------------------------

**Filter by shelf**::

    record-shelf generate --username YOUR_DISCOGS_USERNAME --shelf "Vinyl"

**Change output format**::

    record-shelf generate --username YOUR_DISCOGS_USERNAME --format csv

**Specify output filename**::

    record-shelf generate --username YOUR_DISCOGS_USERNAME --output my_collection.xlsx

**Enable debug logging**::

    record-shelf --debug generate --username YOUR_DISCOGS_USERNAME

Common Examples
---------------

Here are some common use cases:

**Vinyl collection to Excel**::

    record-shelf generate --username myuser --shelf "Vinyl" --output vinyl_collection.xlsx

**Complete collection to CSV**::

    record-shelf generate --username myuser --format csv --output complete_collection.csv

**HTML report for web viewing**::

    record-shelf generate --username myuser --format html --output collection.html

**Debug a specific shelf**::

    record-shelf --debug generate --username myuser --shelf "CD" --output cd_debug.xlsx

Understanding the Output
------------------------

Record Shelf generates reports with the following columns:

- **Shelf**: Collection folder/shelf name
- **Artist**: Artist name(s)
- **Title**: Release title
- **Label**: Record label(s)
- **Catalog Number**: Label catalog number(s)
- **Format**: Format details (e.g., "Vinyl, LP, Album")
- **Year**: Release year
- **Genre**: Music genre(s)
- **Style**: Music style(s)
- **Country**: Country of release
- **Discogs ID**: Unique Discogs release ID
- **Master ID**: Master release ID (if applicable)
- **Rating**: Your rating (if set)
- **Notes**: Your personal notes (if any)

**Excel Format Features**:

- Main "Collection" sheet with all items
- Separate sheet for each shelf
- Sortable columns and formatting

Troubleshooting
---------------

**Authentication Error**
   - Verify your Discogs token is correct
   - Check if token is set via environment variable or --token option

**Empty Collection**
   - Verify the username is correct
   - Check if the collection is public
   - Ensure the user has items in their collection

**Rate Limiting**
   - Record Shelf includes built-in rate limiting
   - If you see rate limit errors, try again in a few minutes

**Missing Data**
   - Some Discogs entries may have incomplete information
   - This is normal and will show as empty fields in the report

Next Steps
----------

Now that you've generated your first report, explore more features:

- :doc:`usage` - Detailed command reference
- :doc:`configuration` - Advanced configuration options
- :doc:`output_formats` - Learn about different output formats
- :doc:`api/modules` - API reference for developers

