def intercalar_mayus_minus(cadena):
    resultado = ""
    for i, letra in enumerate(cadena):
        if i % 2 == 0:
            resultado += letra.upper()
        else:
            resultado += letra.lower()
    return resultado


cadena_original = input("Ingresa una cadena: ")
cadena_transformada = intercalar_mayus_minus(cadena_original)
print("Cadena transformada:", cadena_transformada)
