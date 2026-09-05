usuario_correcto = "alumno"
clave_correcta = "python123"

acceso1 = False
intentos1 = 0

while intentos1 < 3 and not acceso1:
    intentos1 += 1
    usuario1 = input(f"Intento {intentos1}/3 - Usuario: ")
    clave1 = input("Clave: ")

    if usuario1 == usuario_correcto and clave1 == clave_correcta:
        acceso1 = True
        print("Acceso concedido.")
    else:
        print("Error: credenciales invalidas.")

if not acceso1:
    print("Cuenta bloqueada.")
else:
    salir1 = False
    while not salir1:
        print()
        print("1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
        opcion1_str = input("Opcion: ")

        if not opcion1_str.isdigit():
            print("Error: ingrese un numero valido.")
            continue

        opcion1 = int(opcion1_str)

        if opcion1 < 1 or opcion1 > 4:
            print("Error: opcion fuera de rango.")
            continue

        if opcion1 == 1:
            print("Inscripto")

        elif opcion1 == 2:
            nueva_clave1 = input("Nueva clave: ")
            if len(nueva_clave1) < 6:
                print("Error: minimo 6 caracteres.")
            else:
                confirmacion1 = input("Confirme la nueva clave: ")
                if nueva_clave1 == confirmacion1:
                    clave_correcta = nueva_clave1
                    print("Clave actualizada correctamente.")
                else:
                    print("Error: las claves no coinciden.")

        elif opcion1 == 3:
            print("Cada dia es una nueva oportunidad para aprender algo mas.")

        elif opcion1 == 4:
            salir1 = True
            print("Sesion finalizada.")
