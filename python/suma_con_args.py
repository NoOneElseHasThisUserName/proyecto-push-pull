def suma_con_args(*args):
    resultado = sum(args)
    return resultado


numeros = [5, 10, 15, 20]
resultado = suma_con_args(*numeros)
print(f"La suma es: {resultado}")
