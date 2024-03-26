import logging
import sys
from app.commands import Command
from app.history import History

class ExitCommand(Command):
    def execute(self):
        logging.info("ExitCommand executed successfully.")
        History.add_history("exit", "", "")
        sys.exit("Exiting...")