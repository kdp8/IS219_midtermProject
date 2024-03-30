import csv
import logging
import os
import pandas as pd

class History:
    @classmethod
    def get_history_file_path(cls):
        base_dir = os.environ.get('HISTORY_BASE_DIR', os.getcwd())
        if not os.path.exists(base_dir):
            os.makedirs(base_dir, exist_ok=True)
        return os.path.join(base_dir, 'history.csv')

    @classmethod
    def load_history(cls):
        history_file = cls.get_history_file_path()
        try:
            history = pd.read_csv(history_file)
            print(history)
            logging.info("History loaded successfully.")
        except pd.errors.EmptyDataError:
            logging.error("No columns to parse from file.")
        except Exception as e:
            logging.error(f"Error loading history: {e}")

    @classmethod
    def delete_history(cls, index):
        history_file = cls.get_history_file_path()
        try:
            history = pd.read_csv(history_file)
            history.drop(index=index, inplace=True)
            history.to_csv(history_file, index=False)
            logging.info("History row deleted successfully.")
        except pd.errors.EmptyDataError:
            logging.error("No columns to parse from file.")
        except KeyError:
            logging.error("Index not found in history.")
        except Exception as e:
            logging.error(f"Error deleting history: {e}")

    @classmethod
    def clear_history(cls):
        history_file = cls.get_history_file_path()
        try:
            with open(history_file, 'w', newline='') as csv_file:
                header = ['command', 'param1', 'param2']
                writer = csv.writer(csv_file)
                writer.writerow(header)
            logging.info("History cleared successfully.")
        except Exception as e:
            logging.error(f"Error clearing history: {e}")

    @classmethod
    def add_history(cls, command, param1, param2):
        history_file = cls.get_history_file_path()
        try:
            with open(history_file, 'a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([command, param1, param2])
            logging.info("History entry added successfully.")
        except Exception as e:
            logging.error(f"Error adding entry to history: {e}")
