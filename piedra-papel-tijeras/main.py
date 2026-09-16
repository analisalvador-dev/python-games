import random

def jugar_ronda():
    opciones = ["piedra", "papel", "tijera"]

    jugada_usuario = input("Elige piedra, papel o tijera: ").lower()
    jugada_compu = random.choice(opciones)

    print(f"Tú elegiste: {jugada_usuario}")
    print(f"La compu eligió: {jugada_compu}")

    if jugada_usuario not in opciones:
        print("Opción no válida. Escribe piedra, papel o tijera.")
    elif jugada_usuario == jugada_compu:
        print("¡Empate!")
    elif (jugada_usuario == "piedra" and jugada_compu == "tijera") or \
         (jugada_usuario == "papel" and jugada_compu == "piedra") or \
         (jugada_usuario == "tijera" and jugada_compu == "papel"):
        print("¡Ganaste!")
    else:
        print("Ganó la compu.")


jugar_de_nuevo = "s"

while jugar_de_nuevo == "s":
    jugar_ronda()
    jugar_de_nuevo = input("¿Jugar de nuevo? (s/n): ").lower()

print("Gracias por jugar!")