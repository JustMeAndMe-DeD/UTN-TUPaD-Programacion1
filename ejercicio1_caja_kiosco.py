nombre1 = input("Cliente: ")
while nombre1 == "" or not nombre1.isalpha():
    print("Error: el nombre solo puede contener letras y no puede estar vacio.")
    nombre1 = input("Cliente: ")

cantidad1_str = input("Cantidad de productos: ")
while not cantidad1_str.isdigit() or int(cantidad1_str) <= 0:
    print("Error: ingrese un numero entero mayor a 0.")
    cantidad1_str = input("Cantidad de productos: ")
cantidad1 = int(cantidad1_str)

total_sin_descuento = 0
total_con_descuento = 0.0

for i in range(1, cantidad1 + 1):
    precio1_str = input(f"Producto {i} - Precio: ")
    while not precio1_str.isdigit():
        print("Error: el precio debe ser un numero entero.")
        precio1_str = input(f"Producto {i} - Precio: ")
    precio1 = int(precio1_str)

    descuento1 = input("Descuento (S/N): ")
    while descuento1.lower() not in ("s", "n"):
        print("Error: ingrese S o N.")
        descuento1 = input("Descuento (S/N): ")

    total_sin_descuento += precio1

    if descuento1.lower() == "s":
        precio_final = precio1 * 0.90
    else:
        precio_final = precio1

    total_con_descuento += precio_final

ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad1

print()
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")
