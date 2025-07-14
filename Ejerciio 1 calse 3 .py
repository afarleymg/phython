#solicitar dato
nombre = input("indque su  nombre: ")
apellido = input("indique su apellido: ")
edad = int(input("indique su edad: "))
correo = input("indique su correo: ")
#condiciòn
if nombre !=  "" and apellido != "" and correo != "" and int(edad) > 18:
    print(nombre)
    print(apellido)
    print(edad)
    print(correo)
else:
    print("Error")   