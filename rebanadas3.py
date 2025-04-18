direccion = [
                ["aldo","pizarro","59688888",["san martin","56465","quilicura"]],
                ["victor","vergara","234234",["sagrada familia","123123","puente alto"]],
                ["robinson","barriga","3123156",["ainavillo","4448","la florida"]]
            
            ]
clientes = []
nombre = input ("ingrese su nombre: ")
apallido = input ("ingrese su appelido: ")
numero = input ("ingrese su numero: ")
clientes.append(nombre)
clientes.append(apallido)
clientes.append(numero)

direccionCliente = []
calle = input("ingrese nombre de calle: ")
numeracion = input("ingrese su numeracion de calle: ")
comuna = input("ingrese comuna: ")

direccionCliente.append(calle)
direccionCliente.append(numeracion)
direccionCliente.append(comuna)
clientes.append(direccionCliente)
direccion.append(clientes)
print(direccion)