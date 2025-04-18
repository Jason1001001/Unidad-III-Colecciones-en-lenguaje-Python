personas = [
                [
                    ["aldo","pizarro","59688888"],
                    ["docente","informatico","123"]
                ],
                [
                    ["victor","vergara","234234"],
                    ["alumno","123123","111"]
                ],
                [
                    ["robinson","barriga","3123156"],
                    ["musico","piano","000"]
                ]
                    
           ]
contador = 0
for persona in personas:
    print(f"datos de {personas[contador][0][0]}:")
    for tipo in persona:
        for elemento in tipo:
            print(elemento)
    contador += 1