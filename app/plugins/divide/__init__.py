from decimal import Decimal
import logging
from app.calculator import Calculator
from app.calculator.operations import divide
from app.commands import Command


class DivideCommand(Command):
    def execute(self):
        user_input1 = Decimal(input("> Num1: "))
        user_input2 = Decimal(input("> Num2: "))
        logging.info("DivideCommand executed successfully.")
        print(Calculator.divide(user_input1, user_input2))