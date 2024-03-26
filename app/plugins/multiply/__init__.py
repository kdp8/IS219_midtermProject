from decimal import Decimal
import logging
from app.calculator import Calculator
from app.calculator.operations import multiply
from app.commands import Command
from app.history import History


class MultiplyCommand(Command):
    def execute(self):
        user_input1 = Decimal(input("> Num1: "))
        user_input2 = Decimal(input("> Num2: "))
        logging.info("MultiplyCommand executed successfully.")
        print(Calculator.multiply(user_input1, user_input2))
        History.add_history("multiply", user_input1, user_input2)
