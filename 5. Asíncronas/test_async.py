import asyncio
import pytest

async def obtener_datos():
    await asyncio.sleep(1)
    return "datos obtenidos"

@pytest.mark.asyncio
async def test_obtener_datos():
    resultado = await obtener_datos()
    assert resultado == "datos obtenidos"
