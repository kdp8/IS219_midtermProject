import csv
from decimal import Decimal
import logging
import os
import pandas as pd
from app.calculator import Calculator
from app.calculator.operations import multiply
from app.commands import Command


class HistoryCommand(Command):
    def __init__(self):
        self.history_file = 'history.csv'

    def execute(self):
        if not os.path.exists(self.history_file):
            self.create_history_file()

        options = {
            'load': self.load_history,
            'delete': self.delete_history,
            'clear': self.clear_history
        }
        logging.info("History Command executed successfully.")

        user_input = input("> Your options are load, delete, or clear: ")
        # if user_input in options:
        #     options[user_input]()
        #     # logging.info(f"Subcommand {user_input}-history executed successfully.")
        # else:
        #     # print(f"No such option: {user_input}")
        #     logging.info(f"Subcommand {user_input}-history not executed.")
        try:
            options[user_input]()
        except pd.errors.EmptyDataError:
            logging.error("No columns to parse from file.")
        except Exception as e:
            logging.error(f"Error executing command: {e}")

    def load_history(self):
        # try:
        self.history = pd.read_csv(self.history_file)
        print(self.history)
        logging.info("History loaded successfully.")
        # except pd.errors.EmptyDataError:
        #     logging.error("No columns to parse from file.")

    def delete_history(self):
        index_to_delete = int(input("> Enter the index of the row to delete: "))
        try:
            self.history = pd.read_csv(self.history_file)
            self.history.drop(index=index_to_delete, inplace=True)
            self.history.to_csv(self.history_file, index=False)
            logging.info("History row deleted successfully.")
        except KeyError:
            print("Invalid index format.")
            logging.info("Index not found in history.")

    def clear_history(self):
        self.create_history_file()
        logging.info("History cleared successfully.")

    def create_history_file(self):
        with open(self.history_file, 'w', newline='') as csv_file:
            header = ['command', 'param1', 'param2']
            writer = csv.writer(csv_file)
            writer.writerow(header)