import random
import time

# Variables globales

inventario = {"prod_1": 120, "prod_2": 150}  # Inventario Inicial
intervalo_compra = 3  # Tiempo que pasa entre cada compra​


def simulador(inventario, intervalo_compra):
# Variables internas

    conteo_compra = 0  # Contador que controla la impresión del inventario cada 10 compras
    conteo_proveedor = 0  # Contador que lleva la cuenta de las existencias de los proveedores
    # Contaor que controla los procesos dependientes de las existencias de los proveedores
    bool_proveedor = True

    while True:
        # Verificando que aún hay al menos 1 producto en existencia
        # Si no hay ningún producto para vender, rompe el bucle
        if not inventario:
            print("No quedan más productos en el inventario")
            break
        # Seleccionado el producto para la compra

        producto_compra = random.choice(list(inventario.keys()))
        inventario_compra = inventario[producto_compra]
        #Seleccionando la cantidad para la compra
        cantidad_compra = random.randint(1, 10)
        #Verificando que el producto esté en inventario en la cantidad pedida
        #Procediendo con la compra si es así
        if inventario_compra >= cantidad_compra:
            inventario_compra -= cantidad_compra
            inventario.update({producto_compra: inventario_compra})
            conteo_compra += cantidad_compra
            print("Se han comprado", cantidad_compra, "unidades del", producto_compra)

        #Si la cantidad a ser comprada es mayor a la del inventario y ya no hay más envíos de los proveedores
        #Entonces, se rematará el inventario que queda

        elif inventario_compra < cantidad_compra and not bool_proveedor:
            inventario_compra = 0
            inventario.update({producto_compra: inventario_compra})
            print("Se ha rematado el inventario del", producto_compra)
            inventario.pop(producto_compra)
        #Verificando si ya se hicieron al menos 10 compras
        #print("Conteo actual:", conteo_compra)
        if conteo_compra >= 10:
            conteo_compra -= 10
            print("Se han realizado al menos 10 compras. Mostrando el inventario disponible:")
            for key, value in inventario.items():
                print(f"{key}:{value}")
            # Pidiendo más inventario si llega a menos de 100 unidades un producto
        if bool_proveedor == True:
            if inventario[producto_compra] < 100 and conteo_proveedor < 150:
                inventario.update({producto_compra: inventario_compra + 50})
                conteo_proveedor += 50
                # Mostrando nuevamente el inventario
                print("Se han pedido 50 unidades más de", producto_compra)
                print("Inventario disponible:")
                for key, value in inventario.items():
                    print(f"{key}:{value}")
            elif conteo_proveedor >= 150:
                print("Los proveedores se han quedado sin inventario para reponer el nuestro.")
                bool_proveedor = False
                # Esperando a la siguiente compra
                time.sleep(intervalo_compra)

# EjecucionS​
simulador(inventario, intervalo_compra)
