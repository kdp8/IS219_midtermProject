import logging
import os
from app.commands import Command
from app.history import History


class MenuCommand(Command):
    def execute(self):
        try:
            plugins_dir = os.path.join(os.getcwd(), "app", "plugins")
            directories = [name for name in os.listdir(plugins_dir) if os.path.isdir(os.path.join(plugins_dir, name))]
            print("List of available commands:", directories)
            logging.info("MenuCommand executed successfully.")
            History.add_history("menu", "", "")
        except FileNotFoundError:
            logging.error("An unexpected error occured.")

# Readme & Documentation (video)
# Add history filename/path as an env var