def numeros_Primos(numero):
    i = 1
    cont = 0
    for i in range(1,numero + 1):
        if numero % i == 0:
            cont += i
            if cont > 2 :
                break
    if cont > 2:
        print("No es numero primo")
    else:
        print("Es numero primo")
    
numeros_Primos(6)