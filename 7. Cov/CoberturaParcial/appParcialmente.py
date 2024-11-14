# appParcialmente.py

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

def potencia(a, b):
    return a ** b

def saludo(nombre):
    if nombre:
        return f"Hola, {nombre}!"
    return "Hola, desconocido!"
