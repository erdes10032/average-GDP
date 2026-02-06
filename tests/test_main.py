import pytest
import sys
import os
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import main


class TestMain:
    """Тесты для основного скрипта."""

    def test_main_with_valid_args(self):
        """Тест запуска с корректными аргументами."""
        test_args = [
            "main.py",
            "--files", "file1.csv", "file2.csv",
            "--report", "average-gdp"
        ]

        with patch.object(sys, 'argv', test_args):
            with patch('main.ReportFactory.create_report') as mock_factory:
                mock_report = mock_factory.return_value
                mock_report.generate.return_value = []

                main.main()

                mock_factory.assert_called_once_with('average-gdp', ['file1.csv', 'file2.csv'])
                mock_report.generate.assert_called_once()

    def test_main_missing_files_arg(self):
        """Тест запуска без обязательного аргумента --files."""
        test_args = ["main.py", "--report", "average-gdp"]

        with patch.object(sys, 'argv', test_args):
            with pytest.raises(SystemExit):
                main.main()

    def test_main_missing_report_arg(self):
        """Тест запуска без обязательного аргумента --report."""
        test_args = ["main.py", "--files", "file1.csv"]

        with patch.object(sys, 'argv', test_args):
            with pytest.raises(SystemExit):
                main.main()