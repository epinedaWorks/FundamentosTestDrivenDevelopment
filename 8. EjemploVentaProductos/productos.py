# productos.py

# Base de datos simulada de productos
productos_db = {
    'camisa': {'precio': 20, 'stock': 100},
    'pantalon': {'precio': 30, 'stock': 50},
    'zapatos': {'precio': 50, 'stock': 30}
}

def calcular_precio_total(productos, descuento=0):
    """
    Calcula el precio total de una lista de productos aplicando un descuento.
    """
    total = 0
    for producto, cantidad in productos.items():
        if producto in productos_db:
            total += productos_db[producto]['precio'] * cantidad
    total -= total * (descuento / 100)
    return total

def verificar_stock(productos):
    """
    Verifica si hay suficiente stock para los productos solicitados.
    """
    for producto, cantidad in productos.items():
        if producto in productos_db and productos_db[producto]['stock'] < cantidad:
            return False, f"Stock insuficiente para {producto}"
    return True, "Stock suficiente"
