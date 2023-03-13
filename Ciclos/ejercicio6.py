asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
puntuaciones = []
for asignatura in asignaturas:
    puntaje = input("¿Qué nota has sacado en " + asignatura + "? ")
    puntuaciones.append(puntaje)
for i in range(len(asignaturas)):
    print("En " + asignaturas[i] + " has sacado " + puntuaciones[i])