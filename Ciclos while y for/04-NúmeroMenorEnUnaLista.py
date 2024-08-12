numeros = [44 , 5 , 7, 23, 9, 14 , 10]
num = 0
menor = numeros[0]
while num < len(numeros):
 if numeros[num] < menor:
  menor = numeros[num]
 num += 1
print("El número menor es:", menor)