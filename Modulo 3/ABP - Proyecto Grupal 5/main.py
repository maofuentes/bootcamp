from random import randint
from time import sleep

# Asignación de variables

# Listas con clientes y productos:

listaclientes = [{"nombre": "Miguel", "edad": "27", "id": "1"},
                 {"nombre": "Viviana", "edad": "20", "id": "2"},
                 {"nombre": "Marcelo", "edad": "28", "id": "3"},
                 {"nombre": "Franco", "edad": "25", "id": "4"},
                 {"nombre": "Angel", "edad": "27", "id": "5"},
                 {"nombre": "Antonio", "edad": "30", "id": "6"},
                 {"nombre": "Juan", "edad": "24", "id": "7"},
                 {"nombre": "Pedro", "edad": "78", "id": "8"},
                 {"nombre": "Cristiano", "edad": "45", "id": "9"},
                 {"nombre": "Santiago", "edad": "37", "id": "10"}
                 ]

listaproductos = [{"nombre": "guitarra", "precio": "200000", "id": "1", "color": "rojo"},
                  {"nombre": "bajo", "precio": "300000",
                      "id": "2", "color": "azul"},
                  {"nombre": "teclado", "precio": "250000",
                  "id": "3", "color": "amarillo"},
                  {"nombre": "trompeta", "precio": "350000",
                   "id": "4", "color": "verde"},
                  {"nombre": "violin", "precio": "400000",
                      "id": "5", "color": "lila"}
                  ]

# La siguiente función imprime con un formato indentado todos los objetos tipo diccionario presentes en una lista
# Está pensado para imprimir las variables listaproductos y listaclientes


def impresionlista(lista):
    for diccionario in lista:
        for key in diccionario:
            if key == "nombre":
                print(f"{key}: {diccionario[key]}")
            else:
                print(f"    {key}: {diccionario[key]}")

ventas = {}

# Impresión de la lista de clientes

print("-------------------------------")
print("Impriemiendo lista de clientes:")
impresionlista(listaclientes)
print("-------------------------------")

# Impresión de la lista de productos

print("-------------------------------")
print("Imprimiendo la lista de productos:")
impresionlista(listaproductos)
print("-------------------------------")

# Agregar a un nuevo cliente:

control_agregar_cliente = input("¿Desea agregar a un nuevo cliente? (Sí/No) ")
control_agregar_cliente = control_agregar_cliente.strip().casefold()

# Visual Studio Code me cambió el nombre de las variables y confundió producto con cliente, pero debería funcionar.
# Es una burrada hacer esto sin funciones. Hasta los cavernícolas programaban mejor.

if control_agregar_cliente == "sí" or control_agregar_cliente == "si":
    nombre = input("Ingrese el nombre del cliente por favor: ")
    nombre = nombre.rstrip()
    color = input("Ingrese la edad del cliente: ")
    color = color.rstrip()
    id = str(len(listaclientes) + 1)
    nuevocliente = {"nombre": nombre, "edad": color, "id": id}

    print("Se ha agregado a un nuevo cliente:")
    print("nombre:", nombre, "edad:", color, "id:", id)

    listaclientes.append(nuevocliente)

    # Impresión de la lista de clientes

    print("-------------------------------")
    print("Impriemiendo lista de clientes:")
    impresionlista(listaclientes)
    print("-------------------------------")

# Agregar a un nuevo producto:

control_agregar_producto = input("¿Desea agregar a un nuevo producto? (Sí/No) ")
control_agregar_producto = control_agregar_producto.strip().casefold()

if control_agregar_producto == "sí" or control_agregar_producto == "si":
    nombre = input("Ingrese el nombre del producto por favor: ")
    nombre = nombre.rstrip()
    color = input("Ingrese el color del poducto: ")
    color = color.rstrip()
    precio = input("Ingrese el precio del producto:")
    precio = precio.rstrip()
    id = str(len(listaproductos) + 1)

    nuevoproducto = {"nombre": nombre, "color": color, "precio:": precio, "id": id}

    print("Se ha agregado a un nuevo producto:")
    print("nombre:", nombre, "color:", color, "precio:", precio, "id:", id)

    listaproductos.append(nuevoproducto)

    # Impresión de la lista de clientes

    print("-------------------------------")
    print("Impriemiendo lista de clientes:")
    impresionlista(listaproductos)
    print("-------------------------------")


# Eliminar un cliente

control_eliminar_cliente = input("¿Desea eliminar a un cliente? (Sí/No) ")
control_eliminar_cliente = control_eliminar_cliente.strip().casefold()

if control_eliminar_cliente == "sí" or control_eliminar_cliente == "si":
    eliminarcliente = input("Ingrese la ID del cliente a eliminar:")

    for objeto in listaclientes:

        if objeto["id"] == eliminarcliente:
            listaclientes.remove(objeto)

            # Impresión de la lista de productos

            print("-------------------------------")
            print("Imprimiendo la lista de productos:")
            impresionlista(listaclientes)
            print("-------------------------------")

# Eliminar un producto al azar

print("Eliminando un producto al azar: ")
eliminarprod = str(randint(1, len(listaproductos)))
for producto in listaproductos:
    if producto["id"] == eliminarprod:
        listaproductos.remove(producto)
        print("Se eliminó al azar el producto:", eliminarprod)

# Eliminar el último producto agregado:

print("Se eliminará el último producto de la lista:", listaproductos[-1])
listaproductos.pop()

# Imprimir todas las claves en los diccionarios


print("Imprimiendo todas las llaves:")
print("Diccionarios de clientes:")

for key in listaclientes[0].keys():
    print(key)
    sleep(2)

print("Diccionarios de productos:")

for key in listaproductos[0].keys():
    print(key)
    sleep(3)

print("-------------------------------")

# Imprimir todos los valores de los diccionarios

print("-------------------------------")

print("Imprimiendo todas los valores:")
print("Diccionarios de clientes:")

for dict in listaclientes:
    print(dict.values())        
    sleep(2)

print("Diccionarios de productos:")

for dict in listaproductos:
    print(dict.values())
    sleep(3)

print("-------------------------------")
print("-------------------------------")

# Imprimiendo los ID de los usuarios

print("Imprimiendo todos los ID de los clientes")
for dict in listaclientes:
    print(f"{dict['nombre']}: {dict['id']}")
    dict.update({"id": str(dict["id"]) + "_piloto"})

print("-------------------------------")

# Agregando el '_piloto' ID al final

print("Imprimiendo todos los ID de los clientes con '_piloto' agregado al final >:(")
for dict in listaclientes:
    print(f"{dict['nombre']}: {dict['id']}")

# Eliminando las 4 últimas ID:

for number in range(4):
    listaclientes.pop()

impresionlista(listaclientes)
