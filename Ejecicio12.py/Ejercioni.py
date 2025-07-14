import sqlite3

#Crear o conectar a la base de datos
conn = sqlite3.connect('productos.db')
cursor = conn.cursor()

#Crear la tabla de productos si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL
    )
''')
conn.commit()

#Función para registrar un producto
def registrar_producto():
    try:
        nombre = input("Ingrese el nombre del producto: ").strip()
        if not nombre: 
            raise ValueError("El nombre no puede estar vacío")

        precio = float(input("Ingrese el precio del producto: "))
        if precio <= 0:
            raise ValueError("El Precio debe ser mayor que cero.")
        cursor.execute("INSERT INTO productos (nombre, precio) VALUES (?, ?)", (nombre, precio))
        conn.commit()
        print("Producto registrado correctamente.")

    except ValueError as ve: 
        print("Error:", ve)
    except Exception as e: 
        print("Error inesperado:", e)

#Función para mostrar todos los produsctos
def mostrar_productos():
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    if productos:
        print("\n--- Lista de productos ---")
        for prod in productos:
            print(f"ID: {prod[0]} | Nombre: {prod[1]} | Precio: ${prod[2]:.2f}")
    else: 
        print("No hay productos registrados.")

#MEnú
def menu():
    while True:
        print("\n--- Menú de Nicki ---")
        print("1. Registrar productos")
        print("2. Mostrar productos")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()

conn.close()