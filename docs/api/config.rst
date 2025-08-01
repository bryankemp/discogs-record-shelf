Config Module
=============

.. automodule:: record_shelf.config
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

Configuration Management
------------------------

The Config module handles application configuration, including API tokens,
user agents, and rate limiting settings.

Usage Examples
--------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from record_shelf.config import Config

   # Basic configuration with token
   config = Config(token="your_discogs_token")

   # Configuration with environment variable
   import os
   os.environ['DISCOGS_TOKEN'] = 'your_token'
   config = Config()  # Will use environment variable

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from record_shelf.config import Config

   # Custom configuration
   config = Config(
       token="your_token",
       user_agent="MyCustomApp/2.0",
       rate_limit_delay=2.0,  # 2 second delay between requests
       debug=True
   )

   # Access configuration properties
   print(f"User Agent: {config.user_agent}")
   print(f"Rate Limit: {config.rate_limit_delay}")
   print(f"Headers: {config.discogs_headers}")

Error Handling
~~~~~~~~~~~~~~

.. code-block:: python

   from record_shelf.config import Config

   try:
       # This will raise ValueError if no token is found
       config = Config()
   except ValueError as e:
       print(f"Configuration error: {e}")
       # Handle missing token

Configuration Options
---------------------

.. list-table:: Configuration Parameters
   :widths: 20 20 60
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``token``
     - ``Optional[str]``
     - Discogs API token. If None, will try to get from DISCOGS_TOKEN environment variable.
   * - ``user_agent``
     - ``str``
     - User agent string for API requests. Default: "RecordShelf/1.0"
   * - ``debug``
     - ``bool``
     - Enable debug mode. Default: False
   * - ``rate_limit_delay``
     - ``float``
     - Delay in seconds between API calls. Default: 1.0

Environment Variables
---------------------

.. list-table:: Environment Variables
   :widths: 30 70
   :header-rows: 1

   * - Variable
     - Description
   * - ``DISCOGS_TOKEN``
     - Discogs API token. Used if no token is provided to Config constructor.

Best Practices
--------------

Token Security
~~~~~~~~~~~~~~

- Store tokens in environment variables, not in code
- Use different tokens for development and production
- Rotate tokens regularly
- Never commit tokens to version control

Rate Limiting
~~~~~~~~~~~~~

- Default 1 second delay is conservative and safe
- Increase delay for large collections or slow networks
- Decrease delay only if you're sure about API limits
- Monitor for rate limit errors in logs

Debugging
~~~~~~~~~

- Enable debug mode for troubleshooting
- Check logs for detailed API interaction information
- Use debug mode to understand rate limiting behavior

