'''
Testing history functionalities
'''
import re
import unittest
from unittest.mock import patch, mock_open
import pandas as pd
from app.env_vars import env
from app.history import History
from app.plugins.history import HistoryCommand

class TestHistory(unittest.TestCase):
    """Tests for the History class methods."""

    @patch('pandas.read_csv')
    def test_load_history(self, mock_read_csv):
        """Test loading history from a CSV file."""
        expected_path = env.get_history_file_path('HISTORY_BASE_DIR', 'history.csv')
        mock_df = pd.DataFrame([['add', 1, 2]], columns=['command', 'param1', 'param2'])
        mock_read_csv.return_value = mock_df

        History.load_history()

        mock_read_csv.assert_called_with(expected_path)

    @patch('pandas.read_csv')
    @patch('pandas.DataFrame.to_csv')
    def test_delete_history(self, mock_to_csv, mock_read_csv):
        """Test deleting an entry from the history."""
        expected_path = env.get_history_file_path('HISTORY_BASE_DIR', 'history.csv')
        mock_df = pd.DataFrame([['add', 1, 2], ['subtract', 3, 2]], columns=['command', 'param1', 'param2'])
        mock_read_csv.return_value = mock_df

        History.delete_history(0)

        mock_to_csv.assert_called_with(expected_path, index=False)

    @patch('builtins.open', new_callable=mock_open)
    def test_add_history(self, mock_file_open):
        """Test adding an entry to the history."""
        expected_path = env.get_history_file_path('HISTORY_BASE_DIR', 'history.csv')
        History.add_history('multiply', 4, 5)

        mock_file_open.assert_called_with(expected_path, 'a', newline='')

        written_content = mock_file_open().write.call_args[0][0]
        self.assertTrue(re.search('multiply,4,5', written_content))

    @patch('builtins.open', new_callable=mock_open)
    def test_clear_history(self, mock_file_open):
        """Test clearing the history."""
        expected_path = env.get_history_file_path('HISTORY_BASE_DIR', 'history.csv')
        History.clear_history()

        mock_file_open.assert_called_with(expected_path, 'w', newline='')

        written_content = mock_file_open().write.call_args[0][0]
        self.assertTrue(re.search('command,param1,param2', written_content))


class TestHistoryCommand(unittest.TestCase):
    """Tests for the HistoryCommand class."""

    @patch('builtins.input', side_effect=['load'])
    @patch('app.history.History.load_history')
    def test_execute_load(self, mock_load_history, mock_input):
        """Test executing the 'load' command."""
        command = HistoryCommand()
        command.execute()
        mock_load_history.assert_called_once()

    @patch('builtins.input', side_effect=['delete', '0'])
    @patch('app.history.History.delete_history')
    def test_execute_delete(self, mock_delete_history, mock_input):
        """Test executing the 'delete' command with an index."""
        command = HistoryCommand()
        command.execute()
        mock_delete_history.assert_called_once_with(0)

    @patch('builtins.input', side_effect=['clear'])
    @patch('app.history.History.clear_history')
    def test_execute_clear(self, mock_clear_history, mock_input):
        """Test executing the 'clear' command."""
        command = HistoryCommand()
        command.execute()
        mock_clear_history.assert_called_once()

    @patch('builtins.input', side_effect=['invalid'])
    @patch('logging.error')
    def test_execute_invalid_option(self, mock_logging_error, mock_input):
        """Test executing an invalid command option."""
        command = HistoryCommand()
        command.execute()
        mock_logging_error.assert_called_once()
