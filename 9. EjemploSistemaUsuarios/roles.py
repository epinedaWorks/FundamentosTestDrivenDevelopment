# roles.py

# Diccionario con los roles y sus permisos asociados
ROLES = {
    'admin': ['crear_usuario', 'eliminar_usuario', 'ver_reportes'],
    'editor': ['crear_usuario', 'ver_reportes'],
    'visitante': ['ver_reportes']
}
