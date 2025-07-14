#ingreso de datos
apellido = input("Ingrese el apellido: ")
nombre = input("Ingrese el nombre: ")
correo = input("Ingrese correo  ")
edad = input("Ingrese edad: ")

#formatear nombre  apellido de forma simple

apellido = apellido.title()
nombre = nombre.title()

#limpiar correo de espacio y validar
correo = correo.replace(" ", "")
if correo.count("@") != 1:
    print("correo invalido. Debe contener un solo   @. ")
else:
    #validar y clasificar por edad
    if edad.isdigit():
        edad = int(edad)
        match edad:
            case  _ if edad <  15:
                rango  =  "Niño/a"
            case _ if 15 <= edad <= 18:
                 rango = "Adolescente"
            case _ if edad > 18:
                 rango = "Adulto/a" 
    else:
        print("Edad invàlida. Debe ser un nùmero.")

        # Mostras resultados
        print("\n--- Informacion procesada ---") 
        print(f"Apellido:{apellido}")
        print(f"Nombre:{nombre}")
        print(f"Correo:{correo}") 
        print(f"Rango etario: {range}") 

                                                                               