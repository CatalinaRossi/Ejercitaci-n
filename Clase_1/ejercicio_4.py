#palabra = input("Sr. Usuario, por favor, ingrese una palabra: ")
#longitud_palabra = len(palabra)
#print(longitud_palabra)
#asteriscos = "*" * longitud_palabra
#print(asteriscos)
#print(palabra, " ", asteriscos)

dict_palabras = {}

for palabra in range(3): 
    palabra = input("Sr. Usuario, por favor, ingrese una palabra: ")
    longitud_palabra = len(palabra)
    asteriscos = "*" * longitud_palabra
    dict_palabras[palabra] = asteriscos


print(dict_palabras)