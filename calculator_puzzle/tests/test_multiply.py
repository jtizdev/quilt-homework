import pytest
from calculator import multiply, Calculator


@pytest.fixture(scope='session')
def calc():
    return Calculator()


@pytest.mark.parametrize('a, b, expected', [
    (1, 2, 2),
    (2, 3, 6),
])
def test_multiply(calc, a, b, expected):
    calc.set_function(multiply)
    assert calc.calc(a, b) == expected, f"multiply error {a} * {b} != {expected}"
