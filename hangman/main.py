import random

palabras = ["python", "teclado", "programacion", "variable", "funcion"]

palabra_secreta = random.choice(palabras)
letras_adivinadas = set()
intentos_restantes = 6


def mostrar_progreso(palabra, letras_adivinadas):
    progreso = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            progreso += letra + " "
        else:
            progreso += "_ "
    return progreso


while intentos_restantes > 0:
    print("\n" + mostrar_progreso(palabra_secreta, letras_adivinadas))
    print(f"Intentos restantes: {intentos_restantes}")

    letra = input("Adivina una letra: ").lower()

    if letra in letras_adivinadas:
        print("Ya intentaste con esa letra.")
        continue

    letras_adivinadas.add(letra)

    if letra in palabra_secreta:
        print("¡Bien! Esa letra sí está.")
    else:
        intentos_restantes -= 1
        print("Esa letra no está.")

    if all(letra in letras_adivinadas for letra in palabra_secreta):
        print("\n¡Ganaste! La palabra era:", palabra_secreta)
        break

if intentos_restantes == 0:
    print("\nPerdiste. La palabra era:", palabra_secreta)