from hypothesis import given
from hypothesis.strategies import integers

@given(integers(), integers())
def test_suma_propiedad(a, b):
    assert a + b == b + a
