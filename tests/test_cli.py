"""Tests for CLI module."""

from unittest.mock import MagicMock, patch

import pytest
from click.testing import CliRunner

from record_shelf.cli import cli


class TestCLI:
    """Test cases for CLI functionality."""

    def setup_method(self):
        """Set up test fixtures."""
        self.runner = CliRunner()

    def test_cli_help(self):
        """Test CLI help command."""
        result = self.runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "Record Shelf - Music Collection Reports Tool" in result.output
        assert "generate" in result.output
        assert "list-categories" in result.output

    def test_generate_help(self):
        """Test generate command help."""
        result = self.runner.invoke(cli, ["generate", "--help"])
        assert result.exit_code == 0
        assert "Generate a custom Discogs collection report" in result.output
        assert "--username" in result.output
        assert "--token" in result.output

    def test_list_categories_help(self):
        """Test list-categories command help."""
        result = self.runner.invoke(cli, ["list-categories", "--help"])
        assert result.exit_code == 0
        assert "List all categories" in result.output
        assert "--username" in result.output

    @patch("record_shelf.cli.ReportGenerator")
    @patch("record_shelf.cli.Config")
    def test_generate_command_success(self, mock_config, mock_generator):
        """Test successful generate command."""
        # Setup mocks
        mock_config.return_value = MagicMock()
        mock_gen_instance = MagicMock()
        mock_generator.return_value = mock_gen_instance
        mock_gen_instance.fetch_collection_data.return_value = [
            {"artist": "Test Artist", "title": "Test Album"}
        ]

        result = self.runner.invoke(
            cli,
            [
                "generate",
                "--token",
                "test_token",
                "--username",
                "testuser",
                "--output",
                "test.xlsx",
            ],
        )

        assert result.exit_code == 0
        assert "Fetching collection for user: testuser" in result.output
        assert "Report saved to: test.xlsx" in result.output

        # Verify mocks were called
        mock_config.assert_called_once()
        mock_gen_instance.fetch_collection_data.assert_called_once_with(
            "testuser", category_filter=None
        )
        mock_gen_instance.create_report.assert_called_once()

    @patch("record_shelf.cli.ReportGenerator")
    @patch("record_shelf.cli.Config")
    def test_list_categories_command_success(self, mock_config, mock_generator):
        """Test successful list-categories command."""
        # Setup mocks
        mock_config.return_value = MagicMock()
        mock_gen_instance = MagicMock()
        mock_generator.return_value = mock_gen_instance
        mock_gen_instance.get_user_categories.return_value = ["Vinyl", "CD", "Digital"]

        result = self.runner.invoke(
            cli, ["list-categories", "--token", "test_token", "--username", "testuser"]
        )

        assert result.exit_code == 0
        assert "Available categories:" in result.output
        assert "- Vinyl" in result.output
        assert "- CD" in result.output
        assert "- Digital" in result.output

        # Verify mocks were called
        mock_gen_instance.get_user_categories.assert_called_once_with("testuser")

    def test_generate_missing_username(self):
        """Test generate command with missing username."""
        result = self.runner.invoke(cli, ["generate", "--token", "test_token"])

        assert result.exit_code != 0
        assert "Missing option" in result.output or "required" in result.output

    @patch("record_shelf.cli.Config")
    def test_generate_config_error(self, mock_config):
        """Test generate command with config error."""
        mock_config.side_effect = ValueError("Token required")

        result = self.runner.invoke(cli, ["generate", "--username", "testuser"])

        assert result.exit_code == 1
        assert "Error:" in result.output

    def test_debug_flag(self):
        """Test debug flag functionality."""
        with patch("record_shelf.cli.setup_logging") as mock_setup:
            result = self.runner.invoke(cli, ["--debug", "generate", "--help"])
            assert result.exit_code == 0
            mock_setup.assert_called_once_with(True)
