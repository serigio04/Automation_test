import pytest

from src.main import sum, is_bigger_than, login

def test_sum():
    assert sum(2,5) == 7

def test_is_bigger_than():
    assert is_bigger_than(10, 8)

@pytest.mark.parametrize(
    "input_x, input_y, expected",
    [
    (5, 1, 6),
    (6, sum(5,1), 12),
    (sum(12,8), 5, 25),
    (-7, 10, 3)
    ]
)
def test_sum_params(input_x, input_y, expected):
    assert sum(input_x, input_y) == expected

def test_login_pass():
    login_passes = login("Serigio27", "Chicharon2@")
    assert login_passes

def test_login_fail():
    login_fail = login("Em1234", "HolaSoyYO")
    assert not login_fail