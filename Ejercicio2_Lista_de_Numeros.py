def obtener_numeros_usuario():
    
  numeros = []
  while True:
    try:
      entrada = input("Ingrese un número (ingrese 0 para terminar): ")
      numero = int(entrada)
      if numero == 0:
        break
      numeros.append(numero)
    except ValueError:
      print("Entrada inválida. Por favor, ingrese un número entero.")
  return numeros

# Ejemplo de uso:
lista_de_numeros = obtener_numeros_usuario()
print("Números ingresados:", lista_de_numeros)