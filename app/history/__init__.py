import csv
import logging
import os
import pandas as pd

class History:
    history_file = 'history.csv'

    @classmethod
    def load_history(cls):
        try:
            history = pd.read_csv(cls.history_file)
            print(history)
            logging.info("History loaded successfully.")
        except pd.errors.EmptyDataError:
            logging.error("No columns to parse from file.")
        except Exception as e:
            logging.error(f"Error loading history: {e}")

    @classmethod
    def delete_history(cls, index):
        try:
            history = pd.read_csv(cls.history_file)
            history.drop(index=index, inplace=True)
            history.to_csv(cls.history_file, index=False)
            logging.info("History row deleted successfully.")
        except pd.errors.EmptyDataError:
            logging.error("No columns to parse from file.")
        except KeyError:
            logging.info("Index not found in history.")
        except Exception as e:
            logging.error(f"Error deleting history: {e}")

    @classmethod
    def clear_history(cls):
        try:
            with open(cls.history_file, 'w', newline='') as csv_file:
                header = ['command', 'param1', 'param2']
                writer = csv.writer(csv_file)
                writer.writerow(header)
            logging.info("History cleared successfully.")
        except Exception as e:
            logging.error(f"Error clearing history: {e}")

    @classmethod
    def add_history(cls, command, param1, param2):
        try:
            with open(cls.history_file, 'a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([command, param1, param2])
            logging.info("History entry added successfully.")
        except Exception as e:
            logging.error(f"Error adding entry to history: {e}")
