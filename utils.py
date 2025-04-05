import random

def generar_numero_aleatorio(minimo, maximo):
    """Genera y devuelve un número aleatorio entre el mínimo y el máximo dados."""
    numero = random.randint(minimo, maximo)
    print(f"Número generado: {numero}")
    return numero

def mostrar_bienvenida():
    """Muestra un mensaje de bienvenida al jugador."""
    print("=" * 40)
    print("¡Bienvenido al juego de Adivina el Número!")
    print("=" * 40 + "\n") 
