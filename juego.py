import random

def jugar():
    """Función principal que ejecuta el juego de Piedra, Papel o Tijeras."""
    opciones = ["piedra", "papel", "tijeras"]
    print("¡Bienvenido al juego de Piedra, Papel o Tijeras!\n")
    
    jugador = input("Elige: piedra, papel o tijeras: ").lower()
    
    if jugador not in opciones:
        print("Opción inválida. Por favor elige piedra, papel o tijeras.\n")
        return

    computadora = random.choice(opciones)
    print(f"\nLa computadora eligió: {computadora}")

    if jugador == computadora:
        print("¡Empate!\n")
    elif (jugador == "piedra" and computadora == "tijeras") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijeras" and computadora == "papel"):
        print("¡Ganaste!\n")
    else:
        print("¡La computadora gana!\n")

def despedida():
    """Función para mostrar un mensaje de despedida."""
    print("\n Gracias por jugar Piedra, Papel o Tijeras. ¡Hasta la próxima!\n") 
