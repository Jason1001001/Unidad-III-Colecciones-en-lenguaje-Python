# lista de números enteros
numeros = [64, 34, 25, 12, 22, 11, 90]

# Mostramos la lista sin ordenar
print("Lista sin ordenar:", numeros)

# Obtenemos el largo de la lista
largo = len(numeros)

# Recorrer toda la lista
for i in range(largo):
    # Variable para marcar si se realizó un intercambio en esta iteración
    intercambio_realizado = False

    # Recorremos la lista hasta la posición i (que se va reduciendo en cada iteración)
    for j in range(0, largo-i-1):
        # Comparamos los elementos adyacentes
        if numeros[j] > numeros[j+1]:
            # Realizamos intercambio si el elemento actual es mayor que el siguiente
            numeros[j], numeros[j+1] = numeros[j+1], numeros[j]
            intercambio_realizado = True

    # Si no se realizó ningún intercambio en esta iteración,
    # la lista ya está ordenada y se puede salir del bucle
    if not intercambio_realizado:
        break

print("Lista ordenada:    ", numeros)

