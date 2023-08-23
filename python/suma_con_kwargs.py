def suma_con_kwargs(**kwargs):
    resultado = sum(kwargs.values())
    return resultado


numeros = {'num1': 5, 'num2': 10, 'num3': 15, 'num4': 20}
resultado = suma_con_kwargs(**numeros)
print(f"La suma es: {resultado}")
