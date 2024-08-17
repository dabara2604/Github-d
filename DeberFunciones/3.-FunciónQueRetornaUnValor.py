def suma(a, b):
    return a - b
resultado = suma(3, 5)
print(f"La suma es: {resultado}")

#Pdt: me dio curiosidad y quise experimentar profesor
def operaciones(a, b):
    suma = a + b
    resta = a - b
    return suma, resta
resultado_suma, resultado_resta = operaciones(3, 5)
print(f"La suma es: {resultado_suma}")
print(f"La resta es: {resultado_resta}")