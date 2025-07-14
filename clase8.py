#crear el diccionario vacio

productos =  {}

while True: #mostar el contenido del diccionario
    print("\n---contenido actual del discconario de proctiso:")
    for nombre, precio in productos.items():
        print(f"-{nombre}:  ${precio:.2f} ")

        #preguntar si desea continuar
    continuar = input("\nDeseasmagregar im mievo producto? si/no:").strip().lower()
    if continuar != "sí":
        break
    #pedir el dato del producto nuevo

    nombre =input("ingresa el nuevo  producto: ").strip()
    try:
        Precio = float(input("ingrese el precio del prododucto: "))
        productos[nombre] = precio
    except ValueError:
        print("precio invalido. Debe ser un numero.")

        #mostrar el contenido final
print("\nDiccionario final del prodcuito:")
for nombre, precio in productos.items():
    print(f"- {nombre} : ${precio:.2f}")