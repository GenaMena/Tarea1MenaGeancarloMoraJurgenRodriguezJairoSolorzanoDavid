
def minuscula_to_mayuscula(texto):
    if type(texto) == str:   # Verifica el tipo de dato
        if texto.islower():   # Revisa si todos los caracteres son minusculas
            return texto.upper()   # Pasa los caracteres
        else:
            return "Error 2: Se encontraron caracteres en mayuscula"
    else:
        return "Error 1: Tipo de dato no válido"


def buscar_w(texto):
    if type(texto) == str:
        for letra in texto:   # Busca letra por letra
            if letra == 'w':   # Si encuentra una w
                return True
        return False   # Si no encontró
    else:
        return "Error 1: Tipo de dato no válido"


def resta(num1, num2):
    if type(num1) == int and type(num2) == int:   # Verifica el tipo de dato
        resultado = num1 - num2
        if resultado < 0:   # Si es menor a cero
            return "Error 3: Resultado no natural"
        else:
            return resultado
    else:
        return "Error 1: Tipo de dato no válido"
