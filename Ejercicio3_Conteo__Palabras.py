def contarPalabras (cadena):
    diccionario = {}
    palabras = cadena.lower().split()
    for palabra in palabras:
        diccionario[palabra] = palabras.count(palabra)
    return diccionario

resultado = contarPalabras("Hola Hola Hola soy aldo aldo aldo pizarro")
print(resultado)