# Lista para almacenar productos
productos = []

while True:
    print("\nMENÚ Variedades Los Lagartos")
    print("1. Agregar Producto")
    print("2. Visualizar Producto")
    print("3. Buscar Producto")
    print("4. Eliminar Producto")
    print("5. Salir")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        nombre = input("Nombre del producto: ").strip()
        categoria = input("Categoría del producto: ").strip()
        precio = input("Precio del producto (solo números): ").strip()

        if not nombre or not categoria or not precio.isdigit():
            print("Datos incorrectos. Intenta nuevamente.")
        else:
            productos.append([nombre, categoria, int(precio)])
            print("Producto agregado de forma exitosa.")

    elif opcion == "2":
        if not productos:
            print("No se registran productos.")
        else:
            print("\n-- Lista de productos --")
            for i in range(len(productos)):
                print(f"{i + 1}. Nombre: {productos[i][0].title()}, Categoría: {productos[i][1]}, Precio: $ {productos[i][2]}")

    elif opcion == "3":
        if not productos:
            print("No hay productos para buscar.")
        else:
            nombre_buscado = input("Ingresa el nombre del producto: ").strip().lower()
            encontrados = []
            for p in productos:
                if p[0].lower() == nombre_buscado:
                    encontrados.append(p)

            if encontrados:
                print("\n-- Resultados de la Búsqueda --")
                for p in encontrados:
                    print(f"Nombre: {p[0]}, Categoría: {p[1]}, Precio: ${p[2]}")
            else:
                print("Sin resultados encontrados.")

    elif opcion == "4":
        if not productos:
            print("No hay productos registrados.")
        else:
            print("\n-- Lista de productos --")
            for i in range(len(productos)):
                print(f"{i + 1}. Nombre: {productos[i][0]}, Categoría: {productos[i][1]}, Precio: ${productos[i][2]}")

            indice = input("Ingresa el número del producto a eliminar: ")
            if not indice.isdigit():
                print("Entrada incorrecta.")
            else:
                indice = int(indice)
                if 1 <= indice <= len(productos):
                    eliminado = productos.pop(indice - 1)
                    print(f"Producto '{eliminado[0]}' eliminado de forma exitosa.")
                else:
                    print("Número fuera de rango.")

    elif opcion == "5":
        print("Saliendo del programa. ¡Gracias por preferirnos!")
        break

    else:
        print("Opción incorrecta. Intente nuevamente.")