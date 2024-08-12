numero = int(input("Ingreese una factorial: "))
factorial = 1
for num in range(1, numero + 1):
 factorial *= num
print(f"El factorial de {numero} es:", factorial)
