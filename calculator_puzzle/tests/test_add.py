import pytest
from calculator import add, Calculator


@pytest.fixture(scope='session')
def calc():
    return Calculator()


@pytest.mark.parametrize('a, b, expected', [
    (1, 2, 3),
    (3, 4, 7),
])
def test_add(calc, a, b, expected):
    calc.set_function(add)
    assert calc.calc(a, b) == expected, f"add error {a} + {b} != {expected}"
