#Lista para almacenas productos
productos = [] # Lista  productos 

while True:
   print("\nMenú Variedades Los Lagartos  ")
   print("1. Agregar Producto")
   print("2. Visualidar  Producto")
   print("3. Buscar  Producto")
   print("4. Eliminar   Producto")
   print("5. Salir")

   opcion = input("Seleccione una Opción:  ").strip()

   if opcion == "1":

      nombre =input("Nombre del producto: ").strip()
      categoria =input("Categoria  del producto: ").strip()
      precio  =input("Precio del producto (solo numeros enteros): ").strip()
    
      if not nombre or not categoria or not precio.isdigit():
        print("Datos incorrectos. Intenta nuevamente")
      else:
        productos.append([nombre, categoria, int(precio)])
        print("Producto agregado con Éxito.")

   elif opcion == "2":
    if not productos:
        print("No se registrasn productos")
    else:
        print("\n-- Lista de productos --")
        for i in range(len(productos)):
         print(f"{i +1}.  Nombre: {productos[i][0].title()}, categoria: {productos[i][1]}, Precio: $ {productos[i][2]}")

   elif opcion == "3":
      if not  productos:
        print("No hay productos para buscar")
      else:
          nombre_buscado = input("Ingresa nombre del producto: ").strip().lower()
          encontrados =[]
          for p in productos:
             if p[0].lower()== nombre_buscado:
               encontrados.append(p)

          if encontrados:
           print("\n-- Resultados de la Busqueda --")
           for p in encontrados:
                print(f"Nombre: {p[0]}, Categoria: {p[1]}, Precio ${p[2]}") 
          else:
              print("Sin resultados encontrados.")
   elif opcion == "4":
    if not productos: 
       print("no hay productos ")
else:
       print("\n-- Lista de productos -- "  )
       for i in range(len(productos)):
          print(f"{i +1}. Nombre: {productos[i][0]}, Categoria: {productos[i][1]}, Precio: ${productos[i][2]}")

indice = input("ingresa ID del producto a eliminar: ")
if not indice.isdigit():
       print("Entrada icorrecta. ")
else:
       indice = int(indice)  
       if 1<= indice <= len(productos):
          Eliminado =productos.pop(indice - 1)
          print(f"producto {Eliminado[0]}  eliminado de forma exitosa.")
       else:
        print("Numero fuera de rango.")

    elif opcion == "5":
      print("salir del programa. !Gracias por preferirnos!") 
       break

   else:
  print("Opcion incorrecta. ")
      

          

               

