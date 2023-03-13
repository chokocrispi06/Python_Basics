asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
aprovado = []
for asignatura in asignaturas:
    puntaje = float(input("¿Qué nota has sacado en " + asignatura + "?"))
    if puntaje >= 5:
        aprovado.append(asignatura)
for asignatura in aprovado:
    asignaturas.remove(asignatura)
print("Tienes que repetir en " + str(asignaturas))