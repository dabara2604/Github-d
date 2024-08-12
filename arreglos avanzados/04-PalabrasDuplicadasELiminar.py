
palabra = ["Gato" , "Leon" , "Gato" , "Araña" , "Leon" , "Gato" , "Gallina" , "pajaro" , "Pavo"]

palbra_sin_duplicados = []

for letra in palabra:
 if letra not in palbra_sin_duplicados:
  palbra_sin_duplicados.append(letra)

print("Arreglo sin duplicados:", palbra_sin_duplicados)