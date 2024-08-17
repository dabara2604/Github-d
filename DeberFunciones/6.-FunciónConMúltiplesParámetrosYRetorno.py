def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b  
    return suma, resta, multiplicacion 

resultado_suma, resultado_resta, resultado_multiplicacion = operaciones_basicas(8, 3)
print(f"Suma: {resultado_suma}, Resta: {resultado_resta}, Multiplicación: {resultado_multiplicacion}")
