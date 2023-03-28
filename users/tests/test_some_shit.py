import pytest


@pytest.fixture()
def sum_function():
    def wrapper(x, y):
        return x + y

    return wrapper


def test__add_test(sum_function):
    x = y = 5
    assert 10 == sum_function(x, y)
