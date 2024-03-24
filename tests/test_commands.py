"""
Testing all the commands
"""
from decimal import Decimal

import pytest
from app.plugins.exit import ExitCommand
from app.plugins.greet import GreetCommand
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand

def test_greet_command(capfd):
    '''
    Test greet command
    '''
    command = GreetCommand()
    command.execute()
    out, err = capfd.readouterr()  # pylint: disable=unused-variable
    assert out == "Hello, World!\n", "The GreetCommand should print 'Hello, World!'"

def test_addition_functionality(monkeypatch, capfd):
    '''
    Test add command
    '''
    inputs = iter(['3', '5'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    command = AddCommand()
    command.execute()
    out, err = capfd.readouterr()  # pylint: disable=unused-variable
    expected_output = str(Decimal('3') + Decimal('5')) + '\n'
    assert out == expected_output, f"Expected output was '{expected_output}', got '{out}' instead."

def test_subtraction_functionality(monkeypatch, capfd):
    '''
    Test subtract command
    '''
    inputs = iter(['5', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    command = SubtractCommand()
    command.execute()
    out, err = capfd.readouterr()  # pylint: disable=unused-variable
    expected_output = str(Decimal('5') - Decimal('3')) + '\n'
    assert out == expected_output, f"Expected output was '{expected_output}', got '{out}' instead."

def test_multiplication_functionality(monkeypatch, capfd):
    '''
    Test multiply command
    '''
    inputs = iter(['3', '5'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    command = MultiplyCommand()
    command.execute()
    out, err = capfd.readouterr()  # pylint: disable=unused-variable
    expected_output = str(Decimal('3') * Decimal('5')) + '\n'
    assert out == expected_output, f"Expected output was '{expected_output}', got '{out}' instead."

def test_division_functionality(monkeypatch, capfd):
    '''
    Test divide command
    '''
    inputs = iter(['10', '5'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    command = DivideCommand()
    command.execute()
    out, err = capfd.readouterr()  # pylint: disable=unused-variable
    expected_output = str(Decimal('10') / Decimal('5')) + '\n'
    assert out == expected_output, f"Expected output was '{expected_output}', got '{out}' instead."

def test_exit_command():
    '''
    Test exit command
    '''
    command = ExitCommand()
    with pytest.raises(SystemExit) as e:
        command.execute()
    assert str(e.value) == "Exiting...", "The ExitCommand should trigger system exit with 'Exiting...' message"
