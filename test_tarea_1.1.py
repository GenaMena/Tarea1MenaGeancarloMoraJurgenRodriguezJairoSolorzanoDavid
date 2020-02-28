import Tarea_1

def test_minuscula_to_mayuscula():
    assert Tarea_1.minuscula_to_mayuscula("hola mundo")=="HOLA MUNDO"

def test_buscar_w():
    assert Tarea_1.buscar_w("hello world")==True

def test_resta():
    assert Tarea_1.resta(5,2)==3
    
