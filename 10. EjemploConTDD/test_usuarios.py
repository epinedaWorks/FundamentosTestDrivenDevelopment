# test_usuarios.py
import pytest
from usuarios import Usuario

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

# Nueva prueba para la función 'desactivar'
def test_desactivar_usuario():
    usuario = Usuario('Juan', 'admin')
    usuario.desactivar()  # Este método aún no existe
    assert usuario.activo == False  # Esperamos que el usuario ahora esté desactivado


# 1. Ciclo Rojo:
## Ver faltantes
## pytest test_usuarios.py

## Ver cobertura en porcentaje
## pytest --cov=usuarios test_usuarios.py

# 2. Ciclo Verde:
## Descomentar def desactivar
## pytest --cov=usuarios test_usuarios.py

# 3. Refactorizar 