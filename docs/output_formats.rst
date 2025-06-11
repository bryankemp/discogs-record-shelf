Output Formats
==============

Record Shelf supports multiple output formats to suit different use cases.
Each format has its own advantages and is optimized for specific scenarios.

Format Overview
---------------

.. list-table:: Format Comparison
   :widths: 15 20 20 20 25
   :header-rows: 1

   * - Format
     - Extension
     - Best For
     - Features
     - File Size
   * - Excel
     - ``.xlsx``
     - Analysis, Sharing
     - Multiple sheets, Formatting
     - Medium
   * - CSV
     - ``.csv``
     - Data Import, Processing
     - Universal compatibility
     - Small
   * - HTML
     - ``.html``
     - Web viewing, Presentation
     - Browser compatible
     - Medium

Excel Format (.xlsx)
--------------------

The Excel format is the default and most feature-rich output option.

Features
~~~~~~~~

**Multiple Worksheets**:

- **"Collection" sheet**: Contains all items from all shelves
- **Individual shelf sheets**: Separate sheet for each shelf
- **Professional formatting**: Headers, borders, and styling

**Data Organization**:

- Sortable columns
- Freeze panes for easy navigation
- Auto-sized columns
- Consistent formatting

**Excel Compatibility**:

- Works with Microsoft Excel 2010+
- Compatible with LibreOffice Calc
- Google Sheets compatible
- Numbers (Mac) compatible

Usage
~~~~~

.. code-block:: bash

   # Default Excel output
   record-shelf generate --username myuser
   
   # Custom Excel filename
   record-shelf generate --username myuser --output my_collection.xlsx
   
   # Excel is the default format
   record-shelf generate --username myuser --format xlsx

Worksheet Structure
~~~~~~~~~~~~~~~~~~~

**Collection Sheet**:

- Contains all items from all shelves
- Sorted by shelf, then artist, then title
- Includes all data columns

**Individual Shelf Sheets**:

- One sheet per shelf (e.g., "Vinyl", "CD", "Digital")
- Contains only items from that specific shelf
- Same column structure as main sheet
- Sheet names are truncated to 31 characters (Excel limit)

Best Practices
~~~~~~~~~~~~~~

- Use for detailed analysis and reporting
- Great for sharing with non-technical users
- Ideal for presentations and documentation
- Perfect for Excel-based workflows

CSV Format (.csv)
-----------------

The CSV format provides universal compatibility and is ideal for data processing.

Features
~~~~~~~~

**Universal Compatibility**:

- Opens in any spreadsheet application
- Compatible with databases
- Scriptable and automatable
- Human-readable text format

**Data Processing**:

- Easy to import into databases
- Works with data analysis tools
- Compatible with pandas, R, etc.
- Small file size

**Simplicity**:

- Single file with all data
- No formatting overhead
- Fast generation and loading
- Version control friendly

Usage
~~~~~

.. code-block:: bash

   # CSV output
   record-shelf generate --username myuser --format csv --output collection.csv
   
   # CSV with custom filename
   record-shelf generate --username myuser --format csv --output my_data.csv

Data Structure
~~~~~~~~~~~~~~

**Single File**:

- All collection data in one file
- Header row with column names
- One row per collection item
- Comma-separated values

**Column Order**:

1. shelf
2. artist
3. title
4. label
5. catalog_number
6. format
7. year
8. genre
9. style
10. country
11. discogs_id
12. master_id
13. rating
14. notes

Example CSV Output::

   shelf,artist,title,label,catalog_number,format,year,genre,style,country,discogs_id,master_id,rating,notes
   Vinyl,"The Beatles","Abbey Road",Apple,PCS 7088,"Vinyl, LP, Album",1969,Rock,"Pop Rock",UK,123456,78910,,
   CD,"Pink Floyd","Dark Side of the Moon","Harvest",CDP 7 46001 2,"CD, Album",1990,Rock,"Progressive Rock",UK,234567,89012,,

Best Practices
~~~~~~~~~~~~~~

- Use for data analysis and processing
- Ideal for importing into databases
- Perfect for automation scripts
- Great for version control systems
- Choose when file size matters

HTML Format (.html)
-------------------

The HTML format creates web-viewable reports that can be shared easily.

Features
~~~~~~~~

**Web Compatibility**:

- Opens in any web browser
- No additional software required
- Mobile-friendly responsive design
- Professional table styling

**Presentation**:

- Clean, readable layout
- Sortable columns (with JavaScript)
- Professional appearance
- Print-friendly styling

**Sharing**:

- Easy to email or host online
- Self-contained file
- Works offline
- Cross-platform compatible

Usage
~~~~~

.. code-block:: bash

   # HTML output
   record-shelf generate --username myuser --format html --output collection.html
   
   # HTML with custom filename
   record-shelf generate --username myuser --format html --output my_collection.html

HTML Structure
~~~~~~~~~~~~~~

**Document Structure**:

- HTML5 compliant
- Embedded CSS styling
- Responsive table layout
- Professional typography

**Table Features**:

- Header row with column names
- Alternating row colors
- Hover effects
- Responsive breakpoints

**Styling**:

- Clean, modern design
- Professional color scheme
- Mobile-responsive layout
- Print optimization

Example HTML Output:

.. code-block:: html

   <!DOCTYPE html>
   <html>
   <head>
       <title>Record Collection</title>
       <style>
           table { border-collapse: collapse; width: 100%; }
           th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
           th { background-color: #f2f2f2; }
           tr:nth-child(even) { background-color: #f9f9f9; }
       </style>
   </head>
   <body>
       <h1>Music Collection Report</h1>
       <table>
           <thead>
               <tr><th>Shelf</th><th>Artist</th><th>Title</th>...</tr>
           </thead>
           <tbody>
               <tr><td>Vinyl</td><td>The Beatles</td><td>Abbey Road</td>...</tr>
           </tbody>
       </table>
   </body>
   </html>

Best Practices
~~~~~~~~~~~~~~

- Use for quick viewing and sharing
- Ideal for presentations
- Great for non-technical users
- Perfect for web-based workflows
- Choose for visual appeal

Choosing the Right Format
-------------------------

Decision Matrix
~~~~~~~~~~~~~~~

**Choose Excel (.xlsx) when**:

- You need multiple worksheets
- Working with Excel-based workflows
- Sharing with business users
- Need professional formatting
- Want sortable, filterable data

**Choose CSV (.csv) when**:

- Importing into databases
- Using data analysis tools
- Automating data processing
- File size is important
- Need version control compatibility

**Choose HTML (.html) when**:

- Quick viewing in browsers
- Sharing via email or web
- Need mobile compatibility
- Want professional presentation
- No special software requirements

Performance Considerations
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Performance Comparison
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Format
     - Generation Speed
     - File Size
     - Memory Usage
     - Loading Speed
   * - Excel
     - Slow
     - Large
     - High
     - Medium
   * - CSV
     - Fast
     - Small
     - Low
     - Fast
   * - HTML
     - Medium
     - Medium
     - Medium
     - Fast

Multiple Format Generation
--------------------------

You can generate multiple formats from the same data::

   # Generate all formats
   record-shelf generate --username myuser --output collection.xlsx --format xlsx
   record-shelf generate --username myuser --output collection.csv --format csv
   record-shelf generate --username myuser --output collection.html --format html

Automation Script Example::

   #!/bin/bash
   export DISCOGS_TOKEN="your_token"
   USERNAME="your_username"
   DATE=$(date +%Y%m%d)
   
   # Generate all formats with date
   record-shelf generate --username $USERNAME --output "${DATE}_collection.xlsx" --format xlsx
   record-shelf generate --username $USERNAME --output "${DATE}_collection.csv" --format csv
   record-shelf generate --username $USERNAME --output "${DATE}_collection.html" --format html

Customization Options
---------------------

File Naming
~~~~~~~~~~~

- Use descriptive filenames
- Include dates for archival
- Use consistent naming schemes
- Consider automated naming

Examples::

   # Date-based naming
   --output "collection_$(date +%Y%m%d).xlsx"
   
   # Shelf-specific naming
   --output "vinyl_collection.xlsx" --shelf "Vinyl"
   
   # User-specific naming
   --output "${USERNAME}_complete.csv"

Output Directory
~~~~~~~~~~~~~~~~

Organize outputs in directories::

   # Create output directory
   mkdir -p reports/$(date +%Y%m)
   
   # Generate to specific directory
   record-shelf generate --username myuser --output "reports/$(date +%Y%m)/collection.xlsx"

Troubleshooting Output Issues
-----------------------------

Common Problems
~~~~~~~~~~~~~~~

**File Permission Errors**::

   Error: Permission denied
   
   Solutions:
   - Check write permissions on output directory
   - Ensure file isn't open in another application
   - Try different output location

**Corrupt Files**::

   Error: File cannot be opened
   
   Solutions:
   - Check available disk space
   - Ensure process completed successfully
   - Try different output format

**Large File Issues**::

   Warning: Large collection detected
   
   Solutions:
   - Use CSV format for better performance
   - Filter by shelf to reduce size
   - Increase available memory

Validation
~~~~~~~~~~

Validate your output files::

   # Check file was created
   ls -la collection.xlsx
   
   # Check file size (should be > 0)
   du -h collection.xlsx
   
   # Quick content check for CSV
   head -5 collection.csv

