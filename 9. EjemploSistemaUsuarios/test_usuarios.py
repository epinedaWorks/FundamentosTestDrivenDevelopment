# test_usuarios.py
import pytest
from usuarios import Usuario

# Prueba de creación de usuario y verificación de permisos
def test_crear_usuario_admin():
    usuario = Usuario('Juan', 'admin')
    assert usuario.nombre == 'Juan'
    assert usuario.rol == 'admin'

def test_tiene_acceso_admin():
    usuario = Usuario('Juan', 'admin')
    assert usuario.tiene_acceso('crear_usuario') == True
    assert usuario.tiene_acceso('eliminar_usuario') == True
    assert usuario.tiene_acceso('ver_reportes') == True

def test_tiene_acceso_editor():
    usuario = Usuario('Maria', 'editor')
    assert usuario.tiene_acceso('crear_usuario') == True
    assert usuario.tiene_acceso('ver_reportes') == True
    assert usuario.tiene_acceso('eliminar_usuario') == False

def test_tiene_acceso_visitante():
    usuario = Usuario('Luis', 'visitante')
    assert usuario.tiene_acceso('ver_reportes') == True
    assert usuario.tiene_acceso('crear_usuario') == False
    assert usuario.tiene_acceso('eliminar_usuario') == False

def test_rol_invalido():
    usuario = Usuario('Carlos', 'invitado')
    assert usuario.tiene_acceso('ver_reportes') == False


# pytest test_usuarios.py --disable-warnings
# pytest --cov=usuarios --cov-report=term-missing test_usuarios.py
