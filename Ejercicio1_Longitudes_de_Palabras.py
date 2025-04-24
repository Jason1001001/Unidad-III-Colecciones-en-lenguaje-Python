def obtener_longitudes(lista_de_palabras):

  longitudes = []
  for palabra in lista_de_palabras:
    longitudes.append(len(palabra))
  return longitudes

palabras = ["manzana", "banana", "kiwi", "naranja"]
longitudes_palabras = obtener_longitudes(palabras)
print(f"Lista de palabras: {palabras}")
print(f"Longitudes de las palabras: {longitudes_palabras}")