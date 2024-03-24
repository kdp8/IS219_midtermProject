"""
confest.pu
"""
from decimal import Decimal
from faker import Faker
from app.calculator.operations import add, subtract, multiply, divide
#  create faker instance
fake = Faker()

# pylint: disable=comparison-with-callable
def generate_test_data(num_records):
    ''' Generates test data using faker'''
    operations = [add, subtract, multiply, divide]
    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1, fix_len=True))
        operation = fake.random_element(elements=operations)

        if operation == divide:
            b = Decimal(fake.random_number(digits=2, fix_len=True)) if b == 0 else b

        try:
            expected = operation(a, b)
        except ZeroDivisionError:
            continue

        yield a, b, operation, expected


def pytest_addoption(parser):
    '''add --num_records command'''
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate for testing")

def pytest_generate_tests(metafunc):
    '''honeslty still trying to figure out what this is'''
    if "a1" in metafunc.fixturenames and \
       "b1" in metafunc.fixturenames and \
       "operation" in metafunc.fixturenames and \
       "expected" in metafunc.fixturenames:
        num_records = metafunc.config.getoption("num_records")
        metafunc.parametrize("a1,b1,operation,expected", list(generate_test_data(num_records)))
