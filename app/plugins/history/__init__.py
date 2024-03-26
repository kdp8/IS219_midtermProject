import logging
import os
from app.commands import Command
from app.history import History

class HistoryCommand(Command):
    def __init__(self):
        self.history = History()

    def execute(self):
        logging.info("History Command executed successfully.")
        user_input = input("> Your options are load, delete, or clear: ")

        options = {
            'load': self.history.load_history,
            'delete': lambda: self.history.delete_history(int(input("> Enter the index of the row to delete: "))),
            'clear': self.history.clear_history
        }
        options.get(user_input, lambda: logging.error(f"No such option: {user_input}"))()