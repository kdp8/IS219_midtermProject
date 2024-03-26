import logging
from decimal import Decimal
from app.calculator import Calculator
from app.calculator.operations import add
from app.commands import Command
from app.history import History

class AddCommand(Command):
    def execute(self):
        user_input1 = Decimal(input("> Num1: "))
        user_input2 = Decimal(input("> Num2: "))
        logging.info("AddCommand executed successfully.")
        print(Calculator.add(user_input1, user_input2))
        History.add_history("add", user_input1, user_input2)
