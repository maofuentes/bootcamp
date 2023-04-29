#se declara inventario con su stock
stock = [
        {"id":1,"nombre":"ZAPATILLAS","cantidad":20},
        {"id":2,"nombre":"POLERAS", "cantidad":10},
        {"id":3,"nombre":"ZAPATOS", "cantidad":15},
        {"id":4,"nombre":"POLERÓN", "cantidad":3},
        {"id":5,"nombre":"CHAQUETA", "cantidad":5},
        {"id":6,"nombre":"GUANTES", "cantidad":4},
]

clientes = [
        {"id":1,"nombre":"Miguel Garay Gallardo","telefono":98547621},
        {"id":2,"nombre":"Franco Valdés Navarro", "telefono":36521478},
        {"id":3,"nombre":"Viviana Vera Ceballos", "telefono":14785296},
        {"id":4,"nombre":"Marcelo Fuentes Oliva", "telefono":36985214},
]

opc_disponible = ""

def validacion():
    """
    Funcion para validar que las opciones digitadas sean correctas
    """
    global opc_disponible
    opcion_ingresada = input()
    while True:
        if opcion_ingresada in opc_disponible:
            return opcion_ingresada 
        else:
            print("Opcion Ingresada no valida")
            opcion_ingresada = input()
    

def manejo_productos():
    """
    Funcion para dotar de funcionalidad a menu de productos
    """
    global opc_disponible
    print("GESTION DE PRODUCTOS")
    print("1)Almacenar nuevos productos.")
    print("2)Actualizar el stock de productos en la bodega virtual.")
    print("3)Mostrar")
    print("Seleccione Opcion: ")
    opc_disponible = "123"
    opcion = int(validacion())
#   codigo para mostrar productos de distinta maneras
    if opcion == 3:
        print("MOSTRAR PRODUCTOS")
        print("1)Mostrar y retornar las unidades disponibles por producto.")
        print("2)Mostrar y retornar las unidades disponibles de un producto en particular.")
        print("3)Mostrar y retornar todos los productos de la tienda.")
        print("4)Mostrar y retornar los productos que tienen más de un número de unidades (escoge el número de unidades).")
        print("Seleccione Opcion: ")
        opc_disponible = "1234"
        opcion_sec = int(validacion())
        if opcion_sec == 1:
            for x in stock:
                print(x["nombre"], x["cantidad"])
        elif opcion_sec == 2:
            for x in stock:
                print(x["id"], x["nombre"])
                opc_disponible = str(x["id"])+opc_disponible
            print("eleccione Producto a Mostrar Stock: ")
            producto = int(validacion())
            print("Quedan",stock[producto-1]['cantidad'],"Productos en Stock")
        elif opcion_sec == 3:
            print("LISTA DE TODOS LOS PRODUCTOS:")
            for x in stock:
                print(x["id"], x["nombre"],"Stock:",x["cantidad"])
        elif opcion_sec == 4:
            print("Seleccione la cantidad minima de unidades: ")
            opc_disponible = "0123456789"
            producto = int(validacion())
            for x in stock:
                if x["cantidad"]>producto:
                    print(x["id"], x["nombre"],"Stock:",x["cantidad"])
#opcion para actualizar stock de productos
    elif opcion == 2:
        print("ACTUALIZAR STOCK")
        for x in stock:
            print(x["id"], x["nombre"])
            opc_disponible = str(x["id"])+opc_disponible
        print("Seleccione Producto para actualizar stock: ")
        opcion_sec = int(validacion())
        opc_disponible = "0123456789"
        print("Ingrese la nueva cantidad de unidades: ")
        cantidad = int(validacion())
        stock[opcion_sec-1]['cantidad'] = cantidad
        for x in stock:
            print(x["id"], x["cantidad"])
#codigo para almacenar nuevos productos
    elif opcion == 1:
        print("ALMACENAR NUEVOS PRODUCTOS")      
        producto = input("Ingrese Nombre de Producto: ")
        print("Ingrese cantidad en stock:")
        opc_disponible = "0123456789"
        cantidad = int(validacion())
        ultimo = len(stock)
        producto_nuevo = {"id":ultimo+1,"nombre":producto,"cantidad":cantidad}
        stock.append(producto_nuevo)

#funcion de manejo de clientes
def manejo_clientes():
    """
    Funcion para dotar de funcionalidad a menu de clientes
    """
    print("GESTION DE CLIENTES")
    print("1)Mostrar clientes registrados.")
    print("2)Ingreso de ventas.")
    global opc_disponible
    opc_disponible = "12"
    opcion = int(validacion())
    if opcion == 1:
        print("CLIENTES REGISTRADOS")
        print("          NOMBRE        TELEFONO")
        for x in clientes:
            print(x["id"], x["nombre"], x["telefono"])
        print("Tenemos un total de ",len(clientes),"Clientes registrados")
    elif opcion == 2:
        print("INGRESO DE VENTAS")
        print("Seleccione Cliente que realizará la compra:")
        print("          NOMBRE        TELEFONO")
        for x in clientes:
            print(x["id"], x["nombre"], x["telefono"])
        opc_disponible  = ""
        #contador de cantidad de clientes registrados para entregar opciones
        for i in range(0, len(clientes)):
            opc_disponible += str(i+1)
        opcion = int(validacion())
        print("Seleccione el producto a comprar (ingrese su numero):")
        for x in stock:
            print(x["id"], x["nombre"], x["cantidad"])
        opc_disponible  = ""
        #contador de cantidad de productos para entregar las opciones
        for i in range(0, len(stock)):
            opc_disponible += str(i+1)
        opcion = int(validacion())
        for x in stock:
            if x["id"] == opcion:
                print("Para este producto tenemos el siguiente Stock:", x["cantidad"])
                while True:
                    cantidad_compra = input("Ingrese la cantidad a comprar: ")
                    if cantidad_compra.isdigit():
                        if int(cantidad_compra) > int(x["cantidad"]):
                            print("ha seleccionado mayor al stock, vuelva a intentar")
                        else:
                            print("Stock disponible")
                            producto_disp = True
                            break
                    else:
                        print("Ingrese solo numeros") 
                if producto_disp == True:
                    print("Por favor confirme la compra (s/n)")
                    opc_disponible = "sn"
                    opcion = validacion()
                    if opcion == "s":
                        print("Compra aprobada y en camino")
                        x["cantidad"] = int(x["cantidad"]) - int(cantidad_compra) 
                    else:
                        print("Compra rechazada por el usuario")



#funcionamiento principal del programa
while True:
    print("*******************************************************************")
    print("********Bienvenido a Pograma de Gestion de Ventas y Bodega*********")
    print("*******************************************************************")
    print("Seleccione que desea hacer: 1)Control de Ventas 2)Control de Bodega")
    opc_disponible = "12"
    opcion = int(validacion())
    if opcion == 2:
        manejo_productos()
    elif opcion == 1:
        manejo_clientes()