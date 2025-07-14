import sqlite3
from colorama import Fore, init

init(autoreset=True)

# Conectar
conn = sqlite3.connect("inventario.db")
cursor = conn.cursor()

# Crear la tabla de productos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL,
        categoria TEXT
    )
''')
conn.commit()

# Función para registrar productos nuevos
def registrar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio: "))
    categoria = input("Ingrese la categoría: ")

    cursor.execute('''
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
    ''', (nombre, descripcion, cantidad, precio, categoria))
    conn.commit()
    print(Fore.GREEN + "✅ Producto registrado con éxito.")

# Función para ver todos los productos
def ver_productos():
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    if productos:
        print("\n📦 Productos en inventario:")
        for p in productos:
            print(f"ID: {p[0]} | Nombre: {p[1]} | Descripción: {p[2]} | Cantidad: {p[3]} | Precio: ${p[4]:.2f} | Categoría: {p[5]}")
    else:
        print(Fore.RED + "⚠️ No hay productos registrados.")

# Función para actualizar productos
def actualizar_productos():
    id_producto = int(input("Ingrese el ID del producto a actualizar: "))
    campo = input("¿Qué campo desea actualizar? (nombre, descripcion, cantidad, precio, categoria): ").strip().lower()
    nuevo_valor = input("Ingrese el nuevo valor: ")

    if campo not in ["nombre", "descripcion", "cantidad", "precio", "categoria"]:
        print(Fore.RED + "❌ Campo no válido.")
        return

    if campo in ["cantidad"]:
        nuevo_valor = int(nuevo_valor)
    elif campo in ["precio"]:
        nuevo_valor = float(nuevo_valor)

    cursor.execute(f'''
        UPDATE productos SET {campo} = ? WHERE id = ?
    ''', (nuevo_valor, id_producto))
    conn.commit()
    print(Fore.GREEN + "✅ Producto actualizado correctamente.")

# Función para eliminar un producto por ID
def eliminar_producto():
    id_producto = int(input("Ingrese el ID del producto a eliminar: "))
    cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
    conn.commit()
    print(Fore.GREEN + "✅ Producto eliminado correctamente.")

# Función para buscar producto por ID, nombre o categoría
def buscar_producto():
    criterio = input("Buscar por (id/nombre/categoria): ").strip().lower()
    valor = input("Ingrese el valor de búsqueda: ")

    if criterio == "id":
        cursor.execute("SELECT * FROM productos WHERE id = ?", (int(valor),))
    elif criterio == "nombre":
        cursor.execute("SELECT * FROM productos WHERE nombre LIKE ?", ("%" + valor + "%",))
    elif criterio == "categoria":
        cursor.execute("SELECT * FROM productos WHERE categoria LIKE ?", ("%" + valor + "%",))
    else:
        print(Fore.RED + "❌ Criterio no válido.")
        return

    resultados = cursor.fetchall()
    if resultados:
        for p in resultados:
            print(f"ID: {p[0]} | Nombre: {p[1]} | Descripción: {p[2]} | Cantidad: {p[3]} | Precio: ${p[4]:.2f} | Categoría: {p[5]}")
    else:
        print(Fore.RED + "⚠️ No se encontraron productos.")

# Función para generar reporte de bajo stock
def reporte_bajo_stock():
    limite = int(input("Ingrese el límite de cantidad para el reporte: "))
    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
    productos = cursor.fetchall()

    if productos:
        print("\n📉 Productos con bajo stock:")
        for p in productos:
            print(f"ID: {p[0]} | Nombre: {p[1]} | Cantidad: {p[3]}")
    else:
        print(Fore.GREEN + "✅ Todos los productos tienen suficiente stock.")

# Menú principal
def menu():
    while True:
        print("\n🧾 Menú Inventario")
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Buscar producto")
        print("6. Reporte de stock")
        print("7. Salir")

        opcion = input("Seleccioná una opción del menú: ")

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            ver_productos()
        elif opcion == "3":
            actualizar_productos()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            buscar_producto()
        elif opcion == "6":
            reporte_bajo_stock()
        elif opcion == "7":
            print(Fore.CYAN + "👋 Saliendo del programa...")
            break
        else:
            print(Fore.RED + "❌ Opción inválida. Intente de nuevo.")

# Ejecutar si este archivo es el principal
if __name__ == "__main__":
    menu()
    conn.close()
