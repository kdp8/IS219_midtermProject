import logging
from app.commands import Command
from app.history import History


class GreetCommand(Command):
    def execute(self):
        logging.info("GreetCommand executed successfully.")
        print("Hello, World!")
        History.add_history("greet", "", "")
        