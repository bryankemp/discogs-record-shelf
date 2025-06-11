"""Tests for config module."""

import os
from unittest.mock import patch

import pytest

from record_shelf.config import Config


class TestConfig:
    """Test cases for Config class."""

    def test_config_with_token(self):
        """Test config creation with explicit token."""
        token = "test_token_123"
        config = Config(token=token)

        assert config.token == token
        assert config.user_agent == "RecordShelf/1.0"
        assert config.debug is False
        assert config.rate_limit_delay == 1.0

    def test_config_with_env_var(self):
        """Test config creation with environment variable."""
        token = "env_token_456"

        with patch.dict(os.environ, {"DISCOGS_TOKEN": token}):
            config = Config()
            assert config.token == token

    def test_config_no_token_raises_error(self):
        """Test that missing token raises ValueError."""
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(ValueError, match="Discogs API token is required"):
                Config()

    def test_config_debug_mode(self):
        """Test config in debug mode."""
        config = Config(token="test", debug=True)
        assert config.debug is True

    def test_discogs_headers(self):
        """Test discogs headers property."""
        token = "test_token"
        config = Config(token=token)

        headers = config.discogs_headers
        assert headers["User-Agent"] == "RecordShelf/1.0"
        assert headers["Authorization"] == f"Discogs token={token}"

    def test_custom_user_agent(self):
        """Test custom user agent."""
        custom_agent = "MyApp/2.0"
        config = Config(token="test", user_agent=custom_agent)

        assert config.user_agent == custom_agent
        assert config.discogs_headers["User-Agent"] == custom_agent

    def test_custom_rate_limit(self):
        """Test custom rate limit delay."""
        custom_delay = 2.5
        config = Config(token="test", rate_limit_delay=custom_delay)

        assert config.rate_limit_delay == custom_delay
