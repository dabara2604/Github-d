import random

def obtener_eleccion_usuario():
    eleccion = input("Elige piedra, papel o tijeras: ").lower()
    while eleccion not in ["piedra", "papel", "tijeras"]:
        eleccion = input("Elección no válida. Por favor, elige piedra, papel o tijeras: ").lower()
    return eleccion

def obtener_eleccion_computadora():
    return random.choice(["piedra", "papel", "tijeras"])

def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "Empate"
    elif (usuario == "piedra" and computadora == "tijeras") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijeras" and computadora == "papel"):
        return "¡Ganaste!"
    else:
        return "Perdiste"

def jugar():
    while True:
        usuario = obtener_eleccion_usuario()
        computadora = obtener_eleccion_computadora()

        print(f"Tu elección: {usuario}")
        print(f"Elección de la computadora: {computadora}")

        resultado = determinar_ganador(usuario, computadora)
        print(resultado)

        jugar_nuevamente = input("¿Quieres jugar otra vez? (si/no): ").lower()
        if jugar_nuevamente != "si":
            break

if __name__ == "__main__":
    jugar()
