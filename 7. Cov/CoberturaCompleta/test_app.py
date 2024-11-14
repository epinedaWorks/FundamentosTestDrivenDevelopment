# test_app.py

import pytest
from app import suma, resta, multiplicacion, division

def test_suma():
    assert suma(3, 4) == 7

def test_resta():
    assert resta(10, 5) == 5

def test_multiplicacion():
    assert multiplicacion(6, 7) == 42

def test_division():
    assert division(10, 2) == 5

def test_division_por_cero():
    with pytest.raises(ValueError):
        division(10, 0)


## pytest --cov=app test_app.py
## pytest --cov=app --cov-report=html
