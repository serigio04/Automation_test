def add(x, y):
    return x + y

def test_addition():
    assert add(1, 2) == 3

def test_addition_negative_numbers():
    assert add(-1, -1) == -2

test_addition()