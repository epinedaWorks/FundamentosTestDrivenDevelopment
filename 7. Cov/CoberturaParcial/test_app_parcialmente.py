# test_app_parcialmente.py

import pytest
from appParcialmente import suma, resta, multiplicacion, division

def test_suma():
    assert suma(2, 3) == 5

def test_resta():
    assert resta(5, 2) == 3

def test_multiplicacion():
    assert multiplicacion(4, 5) == 20

def test_division():
    assert division(10, 2) == 5

def test_division_por_cero():
    with pytest.raises(ValueError):
        division(10, 0)


# pytest --cov=appParcialmente --cov-report=term-missing
