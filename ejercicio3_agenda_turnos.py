lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""


def cupos_dia(dia):
    return 4 if dia == 1 else 3


def obtener_turno(dia, numero):
    if dia == 1:
        if numero == 1:
            return lunes1
        elif numero == 2:
            return lunes2
        elif numero == 3:
            return lunes3
        elif numero == 4:
            return lunes4
    else:
        if numero == 1:
            return martes1
        elif numero == 2:
            return martes2
        elif numero == 3:
            return martes3
    return None


def guardar_turno(dia, numero, valor):
    global lunes1, lunes2, lunes3, lunes4, martes1, martes2, martes3
    if dia == 1:
        if numero == 1:
            lunes1 = valor
        elif numero == 2:
            lunes2 = valor
        elif numero == 3:
            lunes3 = valor
        elif numero == 4:
            lunes4 = valor
    else:
        if numero == 1:
            martes1 = valor
        elif numero == 2:
            martes2 = valor
        elif numero == 3:
            martes3 = valor


def pedir_dia():
    dia_str = input("Elegir dia (1=Lunes, 2=Martes): ")
    while not dia_str.isdigit() or int(dia_str) not in (1, 2):
        print("Error: ingrese 1 (Lunes) o 2 (Martes).")
        dia_str = input("Elegir dia (1=Lunes, 2=Martes): ")
    return int(dia_str)


def pedir_nombre_paciente():
    paciente1 = input("Nombre del paciente: ")
    while paciente1 == "" or not paciente1.isalpha():
        print("Error: el nombre solo puede contener letras.")
        paciente1 = input("Nombre del paciente: ")
    return paciente1


def reservar_turno():
    dia = pedir_dia()
    paciente1 = pedir_nombre_paciente()

    for n in range(1, cupos_dia(dia) + 1):
        if obtener_turno(dia, n) == paciente1:
            print("Error: ese paciente ya tiene un turno reservado ese dia.")
            return

    for n in range(1, cupos_dia(dia) + 1):
        if obtener_turno(dia, n) == "":
            guardar_turno(dia, n, paciente1)
            print(f"Turno reservado: {paciente1} - Turno {n}.")
            return

    print("Error: no hay turnos disponibles ese dia.")


def cancelar_turno():
    dia = pedir_dia()
    paciente1 = pedir_nombre_paciente()

    for n in range(1, cupos_dia(dia) + 1):
        if obtener_turno(dia, n) == paciente1:
            guardar_turno(dia, n, "")
            print(f"Turno de {paciente1} cancelado.")
            return

    print("Error: no se encontro un turno con ese nombre ese dia.")


def ver_agenda_dia():
    dia = pedir_dia()
    nombre_dia = "Lunes" if dia == 1 else "Martes"
    print(f"--- Agenda del {nombre_dia} ---")
    for n in range(1, cupos_dia(dia) + 1):
        valor = obtener_turno(dia, n)
        if valor == "":
            print(f"Turno {n}: (libre)")
        else:
            print(f"Turno {n}: {valor}")


def ver_resumen_general():
    ocupados_lunes = 0
    for n in range(1, cupos_dia(1) + 1):
        if obtener_turno(1, n) != "":
            ocupados_lunes += 1
    libres_lunes = cupos_dia(1) - ocupados_lunes

    ocupados_martes = 0
    for n in range(1, cupos_dia(2) + 1):
        if obtener_turno(2, n) != "":
            ocupados_martes += 1
    libres_martes = cupos_dia(2) - ocupados_martes

    print("--- Resumen general ---")
    print(f"Lunes: {ocupados_lunes} ocupados, {libres_lunes} disponibles.")
    print(f"Martes: {ocupados_martes} ocupados, {libres_martes} disponibles.")

    if ocupados_lunes > ocupados_martes:
        print("Dia con mas turnos ocupados: Lunes.")
    elif ocupados_martes > ocupados_lunes:
        print("Dia con mas turnos ocupados: Martes.")
    else:
        print("Ambos dias tienen la misma cantidad de turnos ocupados (empate).")


operador1 = input("Nombre del operador: ")
while operador1 == "" or not operador1.isalpha():
    print("Error: el nombre solo puede contener letras.")
    operador1 = input("Nombre del operador: ")

cerrar1 = False
while not cerrar1:
    print()
    print("1) Reservar turno  2) Cancelar turno  3) Ver agenda del dia  4) Ver resumen general  5) Cerrar sistema")
    opcion1_str = input("Opcion: ")

    if not opcion1_str.isdigit() or int(opcion1_str) not in (1, 2, 3, 4, 5):
        print("Error: ingrese una opcion valida (1 a 5).")
        continue

    opcion1 = int(opcion1_str)

    if opcion1 == 1:
        reservar_turno()
    elif opcion1 == 2:
        cancelar_turno()
    elif opcion1 == 3:
        ver_agenda_dia()
    elif opcion1 == 4:
        ver_resumen_general()
    elif opcion1 == 5:
        cerrar1 = True
        print("Sistema cerrado.")
