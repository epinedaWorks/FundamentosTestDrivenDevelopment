# usuarios.py

class Usuario:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol
        self.activo = True  # Atributo para verificar si el usuario está activo

    def tiene_acceso(self, permiso):
        # Lógica de verificación de acceso
        permisos = {
            'admin': ['crear_usuario', 'eliminar_usuario', 'ver_reportes'],
            'editor': ['crear_usuario', 'ver_reportes'],
            'visitante': ['ver_reportes']
        }
        if self.rol not in permisos:
            return False
        return permiso in permisos[self.rol]

    #def desactivar(self):
    #    """Implementamos el método desactivar() para pasar la prueba"""
    #    self.activo = False

    def __repr__(self):
        return f"Usuario({self.nombre}, {self.rol})"

# 1. Ciclo Rojo:
## Ver faltantes
## pytest test_usuarios.py

## Ver cobertura en porcentaje
## pytest --cov=usuarios test_usuarios.py

# 2. Ciclo Verde:
## Descomentar def desactivar
## pytest --cov=usuarios test_usuarios.py

# 3. Refactorizar 
