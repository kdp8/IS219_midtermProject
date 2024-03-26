import csv
import logging
import os
import pandas as pd

class History:
    def __init__(self, history_file='history.csv'):
        self.history_file = history_file

    def load_history(self):
        try:
            history = pd.read_csv(self.history_file)
            print(history)
            logging.info("History loaded successfully.")
        except pd.errors.EmptyDataError:
            logging.error("No columns to parse from file.")
        except Exception as e:
            logging.error(f"Error loading history: {e}")

    def delete_history(self, index):
        try:
            history = pd.read_csv(self.history_file)
            history.drop(index=index, inplace=True)
            history.to_csv(self.history_file, index=False)
            logging.info("History row deleted successfully.")
        except pd.errors.EmptyDataError:
            logging.error("No columns to parse from file.")
        except KeyError:
            logging.info("Index not found in history.")
        except Exception as e:
            logging.error(f"Error deleting history: {e}")

    def clear_history(self):
        try:
            with open(self.history_file, 'w', newline='') as csv_file:
                header = ['command', 'param1', 'param2']
                writer = csv.writer(csv_file)
                writer.writerow(header)
            logging.info("History cleared successfully.")
        except Exception as e:
            logging.error(f"Error clearing history: {e}")
