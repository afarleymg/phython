import sqlite3

#conectar
conn = sqlite3.connect("invenatrario.db")
cursor = conn.cursor()

#Crear la tabla de Productos
cursor.execute ('''1
                
    CREATE TABLE IF NOT EXISTS Productos (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       nombre TEXT NOT NULL,
       descripcion TEXT,
       cantidad INTEGER NOT NULL,
       precio REAL NOT NULL,
       categoria TEXT              
    )
''')
conn.commit()

#Funcion para registrar productos nuevos
def registrar_producto():
    nombre = input("Ingrese el nombre del producto:  ")
    descripcion = input("Ingrese la descripcion del producto: ")
    cantidad = int(input("Ingrese la cantidad : "))
    precio = float(input("Ingrese el precio : "))
    categoria =  input("Ingrese la categoria : ")   

    cursor.execute('''  
        INSERTE INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?) ''',(nombre, descripcion, cantidad, precio, categoria))             ))
    conn.comi
    print("producto registrado con exito.  ")
    
    #Funcion paa ver todos los productos
def ver_productos():
     cursor.execute("SELEC = from productos¨")
     productos = cursor.fetchall()

     if productos:
        print("\n Productos en invenatrio:")
        for p in productos:
               print(f"ID: {p[0]}  | Nombre: {p[1]} | Descripcion: {p[2]} | Cantidad: {p[3]} | Precio: ${p[4]:.2f} | Categoria{p[5]} ")
     else:
                print("No hay productos registrados")

       #funcion para actulizar productos   
def actulizar_productos():
      id_producto = int(input("Ingrese el id del producto: "))
      campo =  input(" ¿Que campo queire actualizar (nombre, descripcion, precio)")
      nuevo_valor = input("Ingrese nuevo valor")

      if campo in ["cantidad", "precio"]:
           nuevo_valor = float(nuevo_valor) if campo ==  "precio" else int(nuevo_valor)

cursor.execute(f'''  
    UPDATE productos SET {campo} = ?  WHERE  id = ?
    ''', (nuevo_valor, id_producto))
conn.comit()
print("Producto actulizado correctamente.")

#funcion de elimiar productos de ID
def elimiar_producto():
     id_producto =  int(input("Ingrese ID del producto a eliminar:"))
     cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
     conn.commit() 
     print("Producto eliminado correctamente ")

     #Funcion para buscar producto por ID Nombre o Categoria 

     def buscar_producto():
           criterio = input("Buscar por (id/nombre/categoria): ").strip().lower()
           valor = input("ingrese el valoor de Busqueda: ")

           if criterio =="id":
                 cursor.execute("SELEC * FROM productos WHERE id = ?", (int(valor),) )
           elif criterio == "nombre":
                 cursor.execute("SELEC * FROM productos WHERE nombre LIKE ?" ,("%" + valor + "%",))
           elif criterio == "categoria":     
                  cursor.execute("SELEC * FROM productos WHERE categoria LIKE ?" ,("%" + valor + "%",))
           else:
            print("criterio no valido") 
            return
     resultados = cursor.fetchall()
     if resultados:
           for p in resultados:
                 print(f"ID: {p[0]}  | Nombre: {p[1]} | Descripcion: {p[2]} | Cantidad: {p[3]} | Precio: ${p[4]:.2f} | Categoria{p[5]} ")
     else:
           print("No se encontraron productos")

  #Funcion Reporte bajo stock
  def reporte_bajo_stock():
      limite = int(input("Ingrese Limite de Cantidad: "))
      cursor.execute("SELECT *FROM productos WHERE cantidad <= ?" , (limite,))
      productos = cursor.fetchall()
      if productos:
            print("\n Productos con bajo stock:") 
            for p in productos:
                  print(f"id: {p[0]}, Nombre: {p[1]}, Cantidad{p[3]}")
      else:
        print("Todos los productos tienen suficiente stock: ") 

def menu():
    while True:
     print("\n Menu Inventario ")
     print("1. Registar producto")
     print("2. Mostrar producto")
     print("3. Actualizar producto")
     print("4. Eliminar producto")
     print("5. Buscar producto")
     print("6. Reporte de Stock")
     print("5. Salir")
    
     opcion = input("Seleccioná una opción del Menu: ")

     if opcion == "1":
          registar_producto()
     elif opcion == "2":
         ver_prodcutos() 
     elif opcion =="3":
          actulizar_productos() 
     elif opcion == "4":
          eliminar_producto()
     elif opcion =="5":
         buscar_Producto() 
     elif opcion == "6":
          reporte_bajo_stock()
          elif opcion =="7":
          buscar_producto() 
     elif opcion == "3":
          print("Saliendo del programa...")
          break
     else:
          print(" Opcion invalida. Intente de nuevo.")

    #Ejecuar el menu si este archivo es el principal

    if__name ==" __main__":
    menu()
    com.close()#cierra la conexion
    




          
              
    edad = input("Ingresá la edad del alumno: ").strip()
    curso = input("Ingresá el curso del alumno: ").strip()
 
    if edad.isdigit(): # Validar que la edad sea un número
        agregar_alumno(nombre, int(edad), curso)
    else:
        print("La edad debe ser un número válido.")

 elif opcion == "2":
    mostrar_alumnos()

 elif opcion == "3":
    id_alumno = input("Ingresá el ID del alumno a actualizar: ").strip()
    nuevo_curso = input("Ingresá el nuevo curso: ").strip()
 
    if id_alumno.isdigit():
        actualizar_curso(int(id_alumno), nuevo_curso)
    else:
        print("El ID debe ser un número válido.")

 elif opcion == "4":
    id_alumno = input("Ingresá el ID del alumno a eliminar: ").strip()
 
    if id_alumno.isdigit():
        eliminar_alumno(int(id_alumno))
    else:
        print("El ID debe ser un número válido.")

 elif opcion == "5":
    print("Saliendo del sistema...")
    break
 else:
    print("Opción inválida. Intentá nuevamente.")             

           
              
        
                                                                