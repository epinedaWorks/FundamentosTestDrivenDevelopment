import pytest

@pytest.mark.parametrize("a, b, resultado", [(1, 2, 3), (5, 5, 10), (-1, -1, -2)])
def test_suma(a, b, resultado):
    assert a + b == resultado
