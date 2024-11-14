def es_par(num):
    return num % 2 == 0

def test_es_par():
    assert es_par(4) is True
    assert es_par(7) is False
