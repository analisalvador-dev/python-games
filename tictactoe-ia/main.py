def tablero_vacio():
    return [" "] * 9


def hay_ganador(tablero, jugador):
    combinaciones = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columnas
        [0, 4, 8], [2, 4, 6]              # diagonales
    ]

    for combo in combinaciones:
        a, b, c = combo
        if tablero[a] == tablero[b] == tablero[c] == jugador:
            return True

    return False


def hay_empate(tablero):
    return " " not in tablero and not hay_ganador(tablero, "X") and not hay_ganador(tablero, "O")


def minimax(tablero, es_turno_ia):
    if hay_ganador(tablero, "O"):
        return 1
    if hay_ganador(tablero, "X"):
        return -1
    if hay_empate(tablero):
        return 0

    if es_turno_ia:
        mejor_puntaje = -float("inf")
        for i in range(9):
            if tablero[i] == " ":
                tablero[i] = "O"
                puntaje = minimax(tablero, False)
                tablero[i] = " "
                mejor_puntaje = max(mejor_puntaje, puntaje)
        return mejor_puntaje
    else:
        mejor_puntaje = float("inf")
        for i in range(9):
            if tablero[i] == " ":
                tablero[i] = "X"
                puntaje = minimax(tablero, True)
                tablero[i] = " "
                mejor_puntaje = min(mejor_puntaje, puntaje)
        return mejor_puntaje


def mejor_jugada(tablero):
    mejor_puntaje = -float("inf")
    jugada = None

    for i in range(9):
        if tablero[i] == " ":
            tablero[i] = "O"
            puntaje = minimax(tablero, False)
            tablero[i] = " "

            if puntaje > mejor_puntaje:
                mejor_puntaje = puntaje
                jugada = i

    return jugada


def mostrar_tablero(tablero):
    print()
    for fila in range(3):
        inicio = fila * 3
        print(f" {tablero[inicio]} | {tablero[inicio+1]} | {tablero[inicio+2]} ")
        if fila < 2:
            print("---+---+---")
    print()


tablero = tablero_vacio()
juego_terminado = False

print("Tú eres X, la IA es O. Las casillas se numeran del 0 al 8.")

while not juego_terminado:
    mostrar_tablero(tablero)

    posicion = int(input("Elige una casilla (0-8): "))

    if tablero[posicion] != " ":
        print("Esa casilla ya está ocupada.")
        continue

    tablero[posicion] = "X"

    if hay_ganador(tablero, "X"):
        mostrar_tablero(tablero)
        print("¡Ganaste!")
        juego_terminado = True
        continue

    if hay_empate(tablero):
        mostrar_tablero(tablero)
        print("¡Empate!")
        juego_terminado = True
        continue

    posicion_ia = mejor_jugada(tablero)
    tablero[posicion_ia]