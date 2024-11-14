import pytest

@pytest.fixture
def usuario():
    return {"nombre": "admin", "email": "admin@example.com"}

def test_usuario(usuario):
    assert usuario["nombre"] == "admin"
    assert usuario["email"] == "admin@example.com"
