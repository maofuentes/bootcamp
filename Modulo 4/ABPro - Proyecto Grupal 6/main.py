"""
DESARROLLO - Continuación del trabajo.
En vista a nuestro sistema desarrollado anteriormente se solicita lo siguiente:
Incorporar un archivo JSON el cual se encargará de almacenar el stock de productos en un archivo
externo el cual, al momento de correr nuevamente el programa, sea posible acceder al archivo y
verificar la ultima cantidad de stock disponible.
Así mismo se solicita contar con un registro de las ventas (en un archivo externo) que ha realizado el
vendedor, para calcular la comisión que lleva actualmente. La comisión consiste en el 10% de cada
venta.
Cada uno de estos archivos, deberá ir actualizando los valores que posean, ya que la idea de esta
implementación es poder detener el programa y contar con la información ya almacenada una vez se
haya detenido el programa.
Por último, guarde información de forma serializada en otro archivo. La información consiste en el
nombre de usuario y la contraseña de cada proveedor.
Identifique claramente la diferencia entre un archivo XML, JSON y YAML.

"""
import json
import datetime
import os

opc_disponible = "1"
opcion = 0
usuarios = []
productos = []
bodega = []
ventas = []
data = []



def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

#validar opciones para evitar falsos ingresos
def validacion(opc_disponible):
    """
    Funcion para validar que las opciones digitadas sean correctas
    """
    opcion_ingresada = input()
    while True:
        if opcion_ingresada in opc_disponible:
            return opcion_ingresada 
        else:
            print("Opcion Ingresada no valida")
            opcion_ingresada = input()

class BaseDatos:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.tablas = {}
        self.cargar_db()

    def cargar_db(self):
        with open(self.nombre_archivo) as archivo_json:
            data = json.load(archivo_json)
            usuarios = [Usuario(u["id"], u["nick"], u["tipo"], u["clave"], u["telefono"], u["edad"]) for u in data["Usuarios"]]
            productos = [Producto(p["sku"], p["nombre"], p["descripcion"], p["categoria"], p["valor_neto"], p["descuento"]) for p in data["Productos"]]
            bodega = [Bodega(b["id"], b["id_sucursal"], b["sku"], b["stock"], b["id_proveedor"]) for b in data["Bodegas"]]
            ventas = [Ventas(v["id"], v["sku"], v["id_cliente"], v["fecha"], v["cantidad"],v["id_vendedor"], v["valor_producto"]) for v in data["Ventas"]]
            return usuarios, productos, bodega, ventas

    def guardar_db(self, usuarios, productos, bodegas, ventas):
        data = {"Usuarios": [], "Productos": [], "Bodegas": [], "Ventas": []}
        for u in usuarios:
            data["Usuarios"].append({"id": u.id, "nick": u.nick, "tipo": u.tipo, "clave": u.clave, "telefono": u.telefono, "edad": u.edad})
        for p in productos:
            data["Productos"].append({"sku": p.sku, "nombre": p.nombre, "descripcion": p.descripcion, "categoria": p.categoria, "valor_neto": p.valor_neto, "descuento": p.descuento})
        for b in bodegas:
            data["Bodegas"].append({"id": b.id, "id_sucursal": b.id_sucursal, "sku": b.sku, "stock": b.stock, "id_proveedor": b.id_proveedor})
        for v in ventas:
            data["Ventas"].append({"id": v.id, "sku": v.sku, "id_cliente": v.id_cliente, "fecha": v.fecha, "cantidad": v.cantidad, "id_vendedor": v.id_vendedor, "valor_producto": v.valor_producto})
        
        with open(self.nombre_archivo, "w") as archivo_json:
            json.dump(data, archivo_json)

class Sucursal():
    global opc_disponible
    global opcion
    def __init__(self, id, nombre, direccion):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion

    # Métodos de la clase Usuarios

    def mostrar_informacion(self):
        print(f"Informacion de Sucursal {self.nombre}")

class Bodega(Sucursal):
    def __init__(self, id, id_sucursal, sku, stock: int, id_proveedor):
        self.id = id
        self.id_sucursal = id_sucursal
        self.sku = sku
        self.stock = stock
        self.id_proveedor = id_proveedor

    # Métodos de la clase Usuarios

    def mostrar_informacion(self):
        print(f"Informacion de Bodega {self.id} {self.nombre}")


class Producto(Bodega):
    impuesto = 1.19
    def __init__(self, sku, nombre: str, descripcion, categoria: str, valor_neto: int, descuento):
        self.sku = sku
        self.nombre = nombre
        self.descripcion = descripcion
        self.categoria = categoria
        self.valor_neto = valor_neto
        self.descuento = descuento

    # Métodos de la clase Producto

    def mostrar_informacion(self):
        print(f"Informacion de Producto {self.sku} {self.nombre}")
    
    def listar_ofertas(self):
        print("Listando todas las ofertas")
        print("---------------------------------------------------------------------------")
        print("Codigo Nombre        Descripcion Valor                    Descuentos")
        for x in productos:
            if int(x.descuento) > 0:
                print(f"{x.sku} {x.nombre} {x.descripcion}    {int(x.valor_neto)+(int(x.valor_neto)*0.19)}     Tiene un descuento de:{x.descuento}%")
        print("---------------------------------------------------------------------------")

    def listar_productos(self):
        print("Listando todos los productos")
        print("---------------------------------------------------------------------------")
        print("Codigo Nombre        Descripcion Valor")
        for x in productos:
            print(x.sku, x.nombre, x.descripcion, int(x.valor_neto)+(int(x.valor_neto)*0.19))
        print("---------------------------------------------------------------------------")

class Ventas(Producto):
    def __init__(self, id, sku, id_cliente, fecha, cantidad, id_vendedor, valor_producto):
        self.id = id
        self.sku = sku
        self.id_cliente = id_cliente
        self.fecha = fecha
        self.cantidad = cantidad
        self.id_vendedor = id_vendedor
        self.valor_producto = valor_producto

    # Métodos de la clase Ventas

    def vender_producto(self):
        usuario_actual.listar_productos()
        opciones = int(len(productos))
        cantidad_usuarios = int(len(usuarios))
        id_venta = int(len(ventas))
        print("Seleccione El producto a vender","1 -",opciones)
        rango = range(1,opciones+1)
        opciones2 = ''.join(str(i) for i in rango)
        id_producto = int(validacion(opciones2))
        id_producto_nuevo = "0" + str(id_producto)
        #Busca el producto en la lista productos para sacar los datos necesarios
        for x in productos:
            if x.sku == id_producto_nuevo:
                cantidad = input(f"Indique la cantidad de {x.nombre} desea: ")
                valor_total = int(cantidad) *(int(x.valor_neto) * (1 + 19/100))
                print(f"El valor Total es: {valor_total}")
                print("¿Desea continuar con la compra? Opcion: 1)SI     2)NO: ")
                opcion = int(validacion("12"))
                if opcion == 1:
                    usuario_actual.listar_usuarios("Normal")
                    print("Seleccione Nuestro Cliente: ")
                    rango = range(1,cantidad_usuarios+1)
                    opciones2 = ''.join(str(i) for i in rango)
                    id_usuario= int(validacion(opciones2))                    
                    for z in usuarios:
                        if int(z.id) == int(id_usuario):
                            print(f" El Usuario: {z.nick} Telefono: {z.telefono} desea comprar {cantidad} {x.nombre} con un costo total de: {valor_total}")
                            print("¿Desea realizar la venta? Opcion: 1)SI     2)NO: ")
                            opcion = int(validacion("12"))
                            if opcion == 1:
                                fecha_actual = datetime.datetime.now()
                                fecha = fecha_actual.strftime("%d/%m/%Y %H:%M:%S")
                                nueva_venta = Ventas(id_venta, x.sku, z.id, fecha, cantidad, usuario_actual.id, valor_total)
                                ventas.append(nueva_venta)
                                grabar_nuevo = BaseDatos("main.json")
                                grabar_nuevo.guardar_db(usuarios,productos,bodegas,ventas)
                                print(f"Venta realizada por {z.nick} con exito por un monto total de {valor_total}: Su orden de compra es: {id_venta}")
        
    def mostrar_ventas(self, id_vendedor):
        limpiar_pantalla()
        total_comision = 0
        print("¿Como Deseas obtener esta informacion?   1)En Pantalla 2)En archivo de texto (ventas.txt)")
        opcion = int(validacion("12"))
        if opcion == 1:
            for x in usuarios:
                if int(x.id) == int(id_vendedor):
                    vendedor_actual = x.nick
                    print(f"Listando todas las Ventas de Vendedor {vendedor_actual}")
                    print("---------------------------------------------------------------------------")
                    print("Codigo     Fecha                 ID Producto        Valor Producto       Comision")
                    for z in ventas:
                        if int(z.id_vendedor) == int(id_vendedor):
                            print(z.id,"      ", z.fecha,"   ", z.sku,"                ",         z.valor_producto,"           ", z.valor_producto*0.1)
                            total_comision = total_comision+int(z.valor_producto*0.1)
                    print("---------------------------------------------------------------------------")
                    print(f"Total de Comision a Pagar {total_comision}")
                    opcion = input("Presione cualquier tecla para continuar...")
        elif 2:
            with open('ventas.txt', 'w') as f:
                for x in usuarios:
                    if int(x.id) == int(id_vendedor):
                        vendedor_actual = x.nick
                        print(f"Listando todas las Ventas de Vendedor {vendedor_actual}", file=f)
                        print("---------------------------------------------------------------------------", file=f)
                        print("Codigo     Fecha                 ID Producto        Valor Producto       Comision", file=f)
                        for z in ventas:
                            if int(z.id_vendedor) == int(id_vendedor):
                                print(z.id,"      ", z.fecha,"   ", z.sku,"                ",         z.valor_producto,"           ", z.valor_producto*0.1, file=f)
                                total_comision = total_comision+int(z.valor_producto*0.1)
                        print("---------------------------------------------------------------------------", file=f)
                        print(f"Total de Comision a Pagar {total_comision}", file=f)
            input("Archivo Guardado Presione una tecla para continuar...")


        



class Usuario(Ventas):
    global opc_disponible
    global opcion
    def __init__(self, id, nick, tipo, clave, telefono, edad):
        self.id = id
        self.nick = nick
        self.tipo = tipo
        self.clave = clave
        self.telefono = telefono
        self.edad = edad

    # Métodos de la clase Usuario

    def mostrar_nick(self):
        print(f"El Nick del Usuario es: {self.nick}")

    def mostrar_tipo(self):
        print(f"El Usuario tiene privilegios: {self.tipo}")

    def mostrar_id(self):
        print(f"La id de usuario es: {self.id}")
    
    def mostrar_clave(self):
        print(f"La clave de usuario es: {self.clave}")

    def menu(self):
        print(f"**************    Bienvenido {self.nick}    **************")
        print(f"************** Panel de Usuario {self.tipo} **************")

    def listar_usuarios(self, tipo):
        print("Listando todos los Usuarios")
        print("---------------------------------------------------------------------------")
        print("Codigo       Nombre                  Telefono")
        for x in usuarios:
            if x.tipo == tipo:
                print(x.id,"           ", x.nick,"                ",         x.telefono)
        print("---------------------------------------------------------------------------")
    
    #Metodo para la creacion de usuarios
    @staticmethod
    def crear_usuario(usuarios):
        id = len(usuarios) + 1 if usuarios else 1
        nick = input("Indique Nick: ")
        print("Tipo de Usuario 1)Administrador 2)Normal 3)Vendedor):")
        opcion = int(validacion("123"))
        if opcion == 1:
            tipo = "Administrador"
        elif opcion == 2:
            tipo = "Normal"
        elif opcion == 3:
            tipo = "Vendedor"
        clave = input("Ingrese clave: ")
        telefono = input("Telefono de contacto: ")
        edad = input("Edad (Solo Numeros): ")
        nuevo_usuario = Usuario(id, nick, tipo, clave, telefono, edad)
        usuarios.append(nuevo_usuario)
        grabar_nuevo = BaseDatos("main.json")
        grabar_nuevo.guardar_db(usuarios,productos,bodegas,ventas)


#clase normal con menu de la tienda que visualiza un cliente
class Normal(Usuario):
    def menu2(self):
        while True:
            limpiar_pantalla()
            print("******************************************************************************************************************************************************")
            print("******************************************************************************************************************************************************")
            print("******************************************************************************************************************************************************")
            print("*************************                         Seleccione las siguientes Opciones para navegar:                          **************************")
            print("******************************************************************************************************************************************************")
            print("******************************************************************************************************************************************************")
            print("******************************************************************************************************************************************************")
            print("1)Listar Ofertas 2)Listar todos los productos 3)Administrar su cuenta 4)Salir: ")
            print("")
            usuario_actual = Normal(x.id,x.nick, x.tipo, x.clave, x.telefono, x.edad)
            opcion = int(validacion("1234"))
            if opcion == 1:
                usuario_actual.listar_ofertas()
                opcion = input("Presione cualquier tecla para continuar...")
            elif opcion == 2:
                usuario_actual.listar_productos()
                opcion = input("Presione cualquier tecla para continuar...")
            elif opcion == 3:
                usuario_actual.admin_cuenta()
            elif opcion == 4:
                break 

    def admin_cuenta(self):
        print("Seleccion 1)Mostrar NICK 2)Mostrar Clave")
        opcion = int(validacion("12"))
        if opcion == 1:
            usuario_actual.mostrar_nick()
            opcion = input("Presione cualquier tecla para continuar...")
        elif opcion == 2:
            usuario_actual.mostrar_clave()
            opcion = input("Presione cualquier tecla para continuar...")

#clase vendedor con opciones de visualizacion de menu vendedor, esta cuenta hereda de Normal para tener visualizacion de tienda como la ve cliente 
class Vendedor(Normal, Ventas):
    def __init__(self, id, nick, tipo, clave, telefono, edad):
        self.id = id
        self.nick = nick
        self.tipo = tipo
        self.clave = clave
        self.telefono = telefono
        self.edad = edad

    def menu3(self):
        limpiar_pantalla()
        while True:
            print("******************************************************************************************************************************************************")
            print("******************************************************************************************************************************************************")
            print("******************************************************************************************************************************************************")
            print("*************************                          Seleccione las siguientes Opciones para Vender:                          **************************")
            print("******************************************************************************************************************************************************")
            print("******************************************************************************************************************************************************")
            print("******************************************************************************************************************************************************")
            print("")
            print("1)Realizar Venta 2)Listar Ofertas 3)Listar Productos 4)Cancelar Venta **** 5)Salir ****")
            usuario_actual = Vendedor(x.id,x.nick, x.tipo, x.clave, x.telefono, x.edad)
            opcion = int(validacion("12345"))
            if opcion == 1:
                usuario_actual.vender_producto()
            elif opcion == 2:
                usuario_actual.listar_ofertas()
                opcion = input("Presione cualquier tecla para continuar...")
            elif opcion == 3:
                usuario_actual.listar_productos()
                opcion = input("Presione cualquier tecla para continuar...")
            elif opcion == 4:
                print("Cancelar Venta")
                opcion = input("Presione cualquier tecla para continuar...")
            elif opcion == 5:
                break

#clase administrador con menu de administrador
class Administrador(Vendedor,BaseDatos):
    def menu1(self):
        limpiar_pantalla()
        print("******************************************************************************************************************************************************")
        print("******************************************************************************************************************************************************")
        print("******************************************************************************************************************************************************")
        print("*************************                     Seleccione las siguientes Opciones para administrar:                          **************************")
        print("******************************************************************************************************************************************************")
        print("******************************************************************************************************************************************************")
        print("******************************************************************************************************************************************************")
        print("")
        print("1)Menu Usuarios(Ver tienda)  2)Menu Vendedores(Adminiatrar ofertas) 3)Menu Administrador(Modificar Usuarios) 4)Mostrar Nick (Sobreescritura) 5)Salir: ")
    
    def menu_admin(self):
        print("**** Seleccione las siguientes Opciones para administrar: ****")
        print("1)Nuevo usuario  2)Cambiar Clave Usuario 3)Eliminar Usuario: 4)Actualizar base datos en archivo 5)Consolidado de Ventas 6)Salir")
        opcion = int(validacion("12345"))
        if opcion == 1:
            print("***************** Ingreso de Nuevos Usuarios ******************")
            Usuario.crear_usuario(usuarios)
        elif opcion == 2:
            print("Opcion No implementada")
        elif opcion == 3:
            print("Opcion No implementada")
        elif opcion == 4:
            grabar_nuevo = BaseDatos("main.json")
            grabar_nuevo.guardar_db(usuarios,productos,bodegas,ventas)
        elif opcion == 5:
            usuario_actual.listar_usuarios("Vendedor")
            vendedor_seleccionado = input("Selecciona el Vendedor del cual necesita Status de venta:")
            usuario_actual.mostrar_ventas(int(vendedor_seleccionado))
        elif opcion == 6:
            pass

    @staticmethod
    def opciones_administrador():
        while True:
            usuario_actual = Administrador(x.id,x.nick, x.tipo, x.clave, x.telefono, x.edad)
            usuario_actual.menu1()
            opcion = int(validacion("12345"))
            if opcion == 1:
                usuario_actual.menu2()
            elif opcion == 2:
                usuario_actual.menu3()
            elif opcion == 3:
                usuario_actual.menu_admin()
            elif opcion == 4:
                usuario_actual.mostrar_nick()
                opcion = input("Presione cualquier tecla para continuar...")
            elif opcion == 5:
                break           
 

#iniciando las bases de archivo
db_completa = BaseDatos("main.json")
db_cargada = db_completa.cargar_db()
usuarios = db_cargada[0]
productos = db_cargada[1]
bodegas = db_cargada[2]
ventas = db_cargada[3]

while True:
    limpiar_pantalla()
    print("******************************************************************************************************************************************************")
    print("******************************************************************************************************************************************************")
    print("******************************************************************************************************************************************************")
    print("**********************************                          Bienvenidos a la tienda Telecompro                   *************************************")
    print("******************************************************************************************************************************************************")
    print("******************************************************************************************************************************************************")
    print("******************************************************************************************************************************************************")
    print("")
    usuario = input("Ingrese su nombre de usuario aquí: ")
    for x in usuarios:
        nombre = x.nick
        usuario_actual = Usuario(x.id,x.nick, x.tipo, x.clave, x.telefono, x.edad)
        if usuario == nombre:      
            if x.tipo == "Administrador":
                Administrador.opciones_administrador()
            elif x.tipo == "Normal":
                usuario_actual = Normal(x.id,x.nick, x.tipo, x.clave, x.telefono, x.edad)
                usuario_actual.menu2()
            elif x.tipo == "Vendedor":
                usuario_actual = Vendedor(x.id,x.nick, x.tipo, x.clave, x.telefono, x.edad)
                usuario_actual.menu3()