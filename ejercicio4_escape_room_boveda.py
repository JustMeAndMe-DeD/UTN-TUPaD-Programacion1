energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

forzados_seguidos1 = 0
bloqueado1 = False

agente1 = input("Nombre del agente: ")
while agente1 == "" or not agente1.isalpha():
    print("Error: el nombre solo puede contener letras.")
    agente1 = input("Nombre del agente: ")

print(f"--- BIENVENIDO, AGENTE {agente1.upper()} ---")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not bloqueado1:

    print()
    print(f"Energia: {energia} | Tiempo: {tiempo} | Cerraduras abiertas: {cerraduras_abiertas}/3 | Alarma: {alarma}")
    print("1) Forzar cerradura  2) Hackear panel  3) Descansar")
    opcion1_str = input("Opcion: ")

    while not opcion1_str.isdigit() or int(opcion1_str) not in (1, 2, 3):
        print("Error: ingrese un numero valido (1, 2 o 3).")
        opcion1_str = input("Opcion: ")

    opcion1 = int(opcion1_str)

    if opcion1 == 1:
        forzados_seguidos1 += 1

        if forzados_seguidos1 >= 3:
            energia -= 20
            tiempo -= 2
            alarma = True
            print("La cerradura se trabo por forzarla demasiadas veces seguidas. Alarma activada!")
        else:
            energia -= 20
            tiempo -= 2

            if energia < 40:
                riesgo1_str = input("Riesgo de alarma. Elija un numero (1-3): ")
                while not riesgo1_str.isdigit() or int(riesgo1_str) not in (1, 2, 3):
                    print("Error: ingrese un numero valido (1, 2 o 3).")
                    riesgo1_str = input("Riesgo de alarma. Elija un numero (1-3): ")
                riesgo1 = int(riesgo1_str)

                if riesgo1 == 3:
                    alarma = True
                    print("Activaste la alarma!")
                else:
                    cerraduras_abiertas += 1
                    print("Cerradura forzada con exito.")
            else:
                cerraduras_abiertas += 1
                print("Cerradura forzada con exito.")

    elif opcion1 == 2:
        forzados_seguidos1 = 0
        energia -= 10
        tiempo -= 3

        print(">> Hackeando panel...")
        for paso1 in range(1, 5):
            codigo_parcial += "A"
            print(f"Progreso {paso1}/4 - Codigo parcial: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("Codigo completo! Se abrio 1 cerradura automaticamente.")

    elif opcion1 == 3:
        forzados_seguidos1 = 0
        energia += 15
        if energia > 100:
            energia = 100
        tiempo -= 1

        if alarma:
            energia -= 10

        print("Descansaste un momento para recuperar energia.")

    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        bloqueado1 = True

print()
if cerraduras_abiertas == 3:
    print("VICTORIA: abriste las 3 cerraduras a tiempo.")
elif bloqueado1:
    print("DERROTA (bloqueo): la alarma bloqueo el sistema antes de que pudieras escapar.")
else:
    print("DERROTA: te quedaste sin energia o sin tiempo.")
