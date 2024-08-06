def convertir_fecha(fecha):
    # Dividir la entrada en día, mes y año
    dia, mes, año = fecha.split('/')

    
    dia = int(dia)
    mes = int(mes)
    año = int(año)

    return dia, mes, año


fecha = input("Introduce la fecha en el formato día/mes/año (DD/MM/AAAA): ")
dia, mes, año = convertir_fecha(fecha)
print(f"El día es: {dia}, el mes es: {mes}, y el año es: {año}")