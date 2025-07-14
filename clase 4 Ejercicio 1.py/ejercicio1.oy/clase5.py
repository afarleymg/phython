# Lista de clientes, algunos en blanco
clientes = ("ana", "juan", "Maria", "LUCAS", "")

# Recorrer lista con for
for i, cliente in enumerate(clientes):
    posicion = i + 1  # para que empiece desde cliente 1

    if cliente.strip() == "":
        print(f"Cliente {posicion}: Nombre no válido (cadena en blanco).")
    else:
        nombre_formateado = cliente.capitalize()
        print(f"Cliente {posicion}: {nombre_formateado}")
        