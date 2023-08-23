def suma_con_args(*args):
    resultado = sum(args)
    return resultado


'''
NOTA Acerca de *args

En *args se recibe un número indeterminado de argumentos desde cualquier
variable de tipo list o tuple
'''
numeros = [5, 10, 15, 20]
resultado = suma_con_args(*numeros)
print(f"La suma es: {resultado}")
