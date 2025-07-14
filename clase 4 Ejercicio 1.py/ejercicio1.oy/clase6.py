#Listas de productos

productos = ["rosa", "azul", "violeta", "lila"]

#Producto que queremos encontrar 
producto_encuentra = "lila"

#REcorrer la lista bucando ese producto

for color in productos:
    if color == producto_encuentra:
        print("color encontrado:", color)
        break #Detiene el bucle al encontrar el producto
    print("Buscando...")
print("Fin de la busqueda.")
