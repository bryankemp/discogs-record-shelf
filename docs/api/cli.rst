CLI Module
==========

.. automodule:: record_shelf.cli
   :members:
   :undoc-members:
   :show-inheritance:

Command Line Interface
----------------------

The CLI module provides the command-line interface for Record Shelf using the Click framework.

Main Entry Point
~~~~~~~~~~~~~~~~

.. autofunction:: record_shelf.cli.main

Commands
~~~~~~~~

.. autofunction:: record_shelf.cli.cli

.. autofunction:: record_shelf.cli.generate

.. autofunction:: record_shelf.cli.list_shelves

Usage Examples
--------------

Programmatic CLI Usage
~~~~~~~~~~~~~~~~~~~~~~

You can invoke the CLI programmatically:

.. code-block:: python

   from record_shelf.cli import main
   import sys

   # Simulate command line arguments
   sys.argv = ['record-shelf', 'generate', '--username', 'myuser', '--output', 'test.xlsx']
   main()

Click Context Usage
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from click.testing import CliRunner
   from record_shelf.cli import cli

   runner = CliRunner()
   result = runner.invoke(cli, ['generate', '--username', 'testuser', '--output', 'test.xlsx'])
   print(result.output)

Command Documentation
---------------------

.. click:: record_shelf.cli:cli
   :prog: record-shelf
   :nested: full

