print("Introduce cuatro puntuaciones entre 0 y 100:")


puntuacion1 = int(input("Puntuación 1: "))
puntuacion2 = int(input("Puntuación 2: "))
puntuacion3 = int(input("Puntuación 3: "))
puntuacion4 = int(input("Puntuación 4: "))

suma = puntuacion1 + puntuacion2 + puntuacion3 + puntuacion4 
promedio_general = suma /4
print(promedio_general)

if promedio_general >= 90:
    print("A")
elif promedio_general >= 80:
    print("B")
elif promedio_general >= 70:
    print("C")
elif promedio_general >= 60:
    print("D") 
else:
    print("E")   