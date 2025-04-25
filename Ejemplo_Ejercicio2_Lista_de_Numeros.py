def ingresoNumeros ():
  numero = "1"
  listaNumeros = []
  print("Ingresa 0 si no quieres ingresar mas numeros...")"
  while numero != "0":
      numero = input("Ingrese un numero: ")
    if numero != "0":
            listaNumeros.append(numero)
    
    print(listaNumeros) 

ingresoNumeros()   