# Inventario

inventario_inicial = {
    "guitarra": 99,
    "bajo": 19,
    "trompeta": 99
}

inventario_reserva = {
    "guitarra": 0,
    "bajo": 0,
    "trompeta": 0
}
# Mostrar inventario actual

print("El inventario actual es:")
for i in inventario_inicial:
    print(i, inventario_inicial[i])

# Tomar pedido

nombre_articulo = input(
    "Por favor ingrese el artículo que desea comprar (guitarra, bajo o trompeta):")
cantidad_articulo = int(
    input("Por favor ingrese el número que desea de este producto:"))

# Revisar el inventario

# El producto debe estar en el inventario

item_bonus = False

if nombre_articulo.lower() in inventario_inicial:

    if cantidad_articulo > 0 and cantidad_articulo <= inventario_inicial[nombre_articulo] and cantidad_articulo <= 20:

        # Verificar si pide al menos 12 objetos para darle uno extra:

        if cantidad_articulo >= 12 and (cantidad_articulo + 1) <= inventario_inicial[nombre_articulo]:
            cantidad_articulo += 1
            item_bonus = True

        # Cálculo del inventario

        balance_inicial = inventario_inicial[nombre_articulo] - \
            cantidad_articulo
        balance_reserva = inventario_reserva[nombre_articulo] + \
            cantidad_articulo

        # Actualizando el inventario

        inventario_inicial.update({nombre_articulo: balance_inicial})
        inventario_reserva.update({nombre_articulo: balance_reserva})

        # Mensaje de confirmación

        print("Su pedido ha sido procesado.")
        if item_bonus:
            print(
                "Porque su pedido es de al menos 12 unidades, le damos una unidad extra de cortesía:")
        print("Pedido: \n", "Artículo:", nombre_articulo,
              "\n", "Cantidad:", cantidad_articulo)

    # Si el inventario no es suficiente

    elif cantidad_articulo > inventario_inicial[nombre_articulo]:

        print("No hay suficiente cantidad de este artículo para procesar su compra.")
        print("Inventario actual:", nombre_articulo,
              inventario_inicial[nombre_articulo])

    # La cantidad del pedido es mayor a 20 unidades

    elif cantidad_articulo > 20:

        print("No se pueden pedir más de 20 unidades en una transacción.")