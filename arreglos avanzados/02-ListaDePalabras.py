
palabras = ["Guapo", "David", "Miedo", "David", "Leon", "David", "Amsitad", "Parejas"]

palb_a_contar = palabras[1]

contador = 0

for letra in palabras:
 if letra == palb_a_contar:
  contador += 1

print(f"La palabra {palb_a_contar} aparece {contador} vez en el arreglo.")