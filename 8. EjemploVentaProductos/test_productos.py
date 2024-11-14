# test_productos.py
import pytest
from productos import calcular_precio_total, verificar_stock, productos_db

def test_calcular_precio_total_sin_descuento():
    productos = {'camisa': 2, 'pantalon': 1}
    total = calcular_precio_total(productos)
    assert total == 70  # 2 * 20 + 1 * 30 = 70

def test_calcular_precio_total_con_descuento():
    productos = {'camisa': 2, 'zapatos': 1}
    total = calcular_precio_total(productos, descuento=10)
    assert total == 81  # (2 * 20 + 1 * 50) - 10% = 81, no 78

def test_verificar_stock_suficiente():
    productos = {'camisa': 2, 'pantalon': 1}
    disponible, mensaje = verificar_stock(productos)
    assert disponible == True
    assert mensaje == "Stock suficiente"

def test_verificar_stock_insuficiente():
    productos = {'zapatos': 40}  # Solo hay 30 zapatos disponibles
    disponible, mensaje = verificar_stock(productos)
    assert disponible == False
    assert mensaje == "Stock insuficiente para zapatos"

def test_verificar_stock_producto_inexistente():
    productos = {'gorro': 1}  # Producto no existe en el inventario
    disponible, mensaje = verificar_stock(productos)
    assert disponible == True
    assert mensaje == "Stock suficiente"

# pytest test_productos.py --cov=productos --cov-report=term-missing
