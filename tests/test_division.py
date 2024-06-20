from my_funcs.utils import division
import pytest


@pytest.mark.parametrize('a, b, result', [(10, 5, 2), (10, 2, 5), (2, 2, 1)])
def test_division_good(a, b, result):
    assert division(a=a, b=b) == result


@pytest.mark.parametrize('a, b, error', [(10, 0, ZeroDivisionError), (10, '2', TypeError)])
def test_division_errors(a, b, error):
    with pytest.raises(error):
        division(a=a, b=b)
