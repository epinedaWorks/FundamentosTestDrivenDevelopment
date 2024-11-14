# usuarios.py

from roles import ROLES

class Usuario:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol

    def tiene_acceso(self, permiso):
        """
        Verifica si el usuario tiene acceso a un permiso basado en su rol.
        """
        if self.rol not in ROLES:
            return False
        return permiso in ROLES[self.rol]

    def desactivar(self):
        """Nuevo método que no está siendo probado"""
        self.activo = False

    def __repr__(self):
        return f"Usuario({self.nombre}, {self.rol})"

