print ("Bienvenido al sistema de inventario de ProDig - Prospectiva Digital")
inventario = {}

while True:
    print("\n--- Menú ---")
    print("1. Agregar producto")
    print("2. Restar producto")
    print("3. Buscar producto")
    print("4. Ver todo el inventario")
    print("5. Salir")

    opcion =input("Elige una opción de 1 a 5: ")
    if opcion == "1":
        producto = input("Nombre del producto: ").lower()
        cantidad = int(input("Cantidad: "))
        inventario[producto] = cantidad
        print(f"Producto '{producto}' agregado con {cantidad} unidades. ")

    elif opcion == "2":
        producto = input("Nombre del producto a restar: ").lower()
        cantidad_restar = int(input("Cantidad a restar: "))
        if producto in inventario:
            if cantidad_restar <= inventario[producto]:
                inventario[producto] -= cantidad_restar
                print(f"Se restaron {cantidad_restar} unidades de {producto}. quedan {inventario[producto]}.")
            else:
                print("No puedes restar mas unidades de las que hay.")
        else:
            print("El producto no esta en el inventario.")

    elif opcion == "3":
        producto = input("Nombre del producto a buscar: ").lower()
        if producto in inventario:
            print(f"{producto} tiene {inventario[producto]} unidades.")
        else:
            print("Producto no encontrado en el inventario")
    
    elif opcion == "4":
        if not inventario:
            print("Inventario vacio")
        else:
            print("Inventario actual:")
            for prod, cant in inventario.items():
                print(f"{prod}:{cant} unidades")

    elif opcion == "5":
        print("Saliendo del programa, hasta pronto!")
        break
    else:
        print("Opción no valida. Intenta de nuevo")