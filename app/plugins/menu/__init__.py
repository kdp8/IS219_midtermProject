import logging
import os
from app.commands import Command


class MultiplyCommand(Command):
    def execute(self):
        try:
            plugins_dir = os.path.join(os.getcwd(), "app", "plugins")
            directories = [name for name in os.listdir(plugins_dir) if os.path.isdir(os.path.join(plugins_dir, name))]
            print("List of available commands:", directories)
        except FileNotFoundError:
            logging.error("An unexpected error occured.")

# Readme
# Refractor logging stuff
# Documentation (video)
# Testing
# Add history filename/path as an env var