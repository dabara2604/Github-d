def convertir_hora(hora_24):
    
    horas, minutos = map(int, hora_24.split(':'))

   
    if horas >= 12:
        periodo = "PM"
    else:
        periodo = "AM"

    if horas == 0:
        horas = 12
    elif horas > 12:
        horas -= 12

   
    hora_12 = f"{horas}:{minutos:02d} {periodo}"
    return hora_12


hora_24 = input("Introduce la hora en notación de 24 horas (HH:MM): ")
hora_12 = convertir_hora(hora_24)
print("La hora en notación de 12 horas es:", hora_12)