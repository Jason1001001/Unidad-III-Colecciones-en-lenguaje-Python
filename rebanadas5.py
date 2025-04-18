direccion = [
                ["aldo","pizarro","59688888",["san martin","56465","quilicura"]],
                ["victor","vergara","234234",["sagrada familia","123123","puente alto"]],
                ["robinson","barriga","3123156",["ainavillo","4448","la florida"]]
            ]
print("datos de aldo:")
for cliente in direccion:
    for elemento in cliente:
        print(elemento)