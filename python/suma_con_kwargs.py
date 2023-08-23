def suma_con_kwargs(**kwargs):
    resultado = sum(kwargs.values())
    return resultado


'''
NOTA Acerca de **kwargs

En **kwargs se recibe un número indeterminado de argumentos desde cualquier
variable de tipo dict
'''

numeros = {'num1': 5, 'num2': 10, 'num3': 15, 'num4': 20}
resultado = suma_con_kwargs(**numeros)
print(f"La suma es: {resultado}")
