import sqlite3

# Crear o conectar a la base de datos
conexion = sqlite3.connect('productos.db')
cursor = conexion.cursor()

# Crear tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL
    )
''')
conexion.commit()

# Función para registrar producto
def registrar_producto():
    try:
        nombre = input("Ingresa el nombre del producto: ").strip()
    if not nombre:
        raise ValueError("El nombre no puede estar vacìo")
        
    precio = float(input("Ingresa el precio del producto: "))
    if precio <= 0:
            raise ValueError("El nombre no puede estar vacìo")
    if precio <=0:
            raise ValueError("El precio  debe ser mayor a 0")
    cursor.execute("INSERT INTO productos (nombre, preciso) VALUES  (?. ?)",(nombre, precio))
    
    print(" Producto registrado con éxito.")

# Función para mostrar productos
def mostrar_productos():
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    if productos:
        print("\n📦 Productos registrados:")
        for prod in productos:
            print(f"ID: {prod[0]}, Nombre: {prod[1]}, Precio: {prod[2]}")
    else:
        print("📭 No hay productos registrados.")

# Menú principal
def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Salir")

        opcion = input("Elige una opción: ")
        if opcion == '1':
            registrar_producto()
        elif opcion == '2':
            mostrar_productos()
        elif opcion == '3':
            print("¡Hasta luego!")
            break
        else:
            print(" Opción no válida.")

menu()

# Cerrar conexión al final
conexion.close()