numero = int(input("Ingrese un numero: "))
for num in range(1, numero + 1):
 print(" " * (numero - num) + "*" * (2 * num - 1))
 