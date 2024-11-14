# test_mock.py

from unittest.mock import patch
import mi_modulo

@patch.object(mi_modulo, 'obtener_datos_api', return_value={"status": "success", "data": [10, 20, 30]})
def test_obtener_datos_api(mock_api):
    # Llamamos a la función mockeada y verificamos el resultado
    respuesta = mi_modulo.obtener_datos_api()
    assert respuesta["data"] == [10, 20, 30]
    print("Prueba pasada con datos mockeados")

#pytest test_mock.py
