height = int(input("What is your height (cm)? "))
credits = int(input("How many credits do you have? "))
if height >= 137 and credits >= 10:
    print("¡Disfruta el viaje!")
elif credits >= 10:
    print("No eres lo suficientemente alto para viajar")
elif height >= 137:
    print("No tiene suficientes créditos")
else:
    print("No cumples ninguno de los requisitos")