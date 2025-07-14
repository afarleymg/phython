#Lista de  clientes , algunos en blancos

clientes =  ("ana",  "juan" , "Maria" ,  "LUCAS"  "")

#recorres lista con for 

for nombre in range(len(clientes)):
    cliente = clientes [nombre]
    posicion = nombre + 1 # para que empice desde cliente 1

    if cliente.strip()  == "": 
     print(f"cliente {posicion}: Nombre no valido(cadena en blanco). ")
else:
    nombre_formateado = cliente.capitalize()
    print(f"cliente {posicion}:  {nombre_formateado}")
