import re

def contar_frecuencia_palabras(texto):
  texto = texto.lower()
  # Eliminar signos de puntuación utilizando expresiones regulares
  texto = re.sub(r'[^\w\s]', '', texto)
  palabras = texto.split()

  frecuencia = {}
  for palabra in palabras:
    if palabra in frecuencia:
      frecuencia[palabra] += 1
    else:
      frecuencia[palabra] = 1
  return frecuencia

# Ejemplo de uso:
cadena_ejemplo = "Esta es una cadena de ejemplo. Esta cadena tiene algunas palabras repetidas como esta."
conteo_palabras = contar_frecuencia_palabras(cadena_ejemplo)
print(f"Cadena de texto: '{cadena_ejemplo}'")
print("Frecuencia de las palabras:", conteo_palabras)