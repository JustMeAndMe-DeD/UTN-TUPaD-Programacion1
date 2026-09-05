print("--- BIENVENIDO A LA ARENA ---")

nombre_gladiador = input("Nombre del Gladiador: ")
while nombre_gladiador == "" or not nombre_gladiador.isalpha():
    print("Error: Solo se permiten letras.")
    nombre_gladiador = input("Nombre del Gladiador: ")

vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_ataque_pesado = 15
danio_enemigo = 12
turno_gladiador = True

print("=== INICIO DEL COMBATE ===")

juego_activo1 = True

while vida_jugador > 0 and vida_enemigo > 0 and juego_activo1:

    print(f"{nombre_gladiador} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige accion:")
    print("1. Ataque Pesado")
    print("2. Rafaga Veloz")
    print("3. Curar")

    opcion1_str = input("Opcion: ")
    while not opcion1_str.isdigit() or int(opcion1_str) not in (1, 2, 3):
        print("Error: Ingrese un numero valido.")
        opcion1_str = input("Opcion: ")
    opcion1 = int(opcion1_str)

    if opcion1 == 1:
        if vida_enemigo < 20:
            danio_final1 = danio_ataque_pesado * 1.5
            print(">> Golpe Critico!")
        else:
            danio_final1 = float(danio_ataque_pesado)

        vida_enemigo -= danio_final1
        print(f"Atacaste al enemigo por {danio_final1} puntos de dano!")

    elif opcion1 == 2:
        print(">> Inicias una rafaga de golpes!")
        for golpe1 in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de dano")

    elif opcion1 == 3:
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print(f"Te curaste! Vida actual: {vida_jugador}. Pociones restantes: {pociones}.")
        else:
            print("No quedan pociones!")

    if vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        print(f"El enemigo te ataco por {danio_enemigo} puntos de dano!")

    print("=== NUEVO TURNO ===")

print()
if vida_jugador > 0:
    print(f"VICTORIA! {nombre_gladiador} ha ganado la batalla.")
else:
    print("DERROTA. Has caido en combate.")
