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

opc_disponible = "1"
opcion = 0
usuarios = []
productos = []
data = []

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
            return usuarios, productos

    def guardar_db(self, usuarios, productos):
        data = {"Usuarios": [], "Productos": []}
        for u in usuarios:
            data["Usuarios"].append({"id": u.id, "nick": u.nick, "tipo": u.tipo, "clave": u.clave, "telefono": u.telefono, "edad": u.edad})
        for p in productos:
            data["Productos"].append({"sku": p.sku, "nombre": p.nombre, "descripcion": p.descripcion, "categoria": p.categoria, "valor_neto": p.valor_neto, "descuento": p.descuento})
        with open(self.nombre_archivo, "w") as archivo_json:
            json.dump(data, archivo_json)

    def agregar_fila(self, nombre_tabla, fila):
        objeto = {}
        for nombre_columna, valor in fila.items():
            objeto[nombre_columna] = valor
        self.tablas[nombre_tabla].append(objeto)

    def modificar_fila(self, nombre_tabla, indice, fila):
        objeto = {}
        for nombre_columna, valor in fila.items():
            objeto[nombre_columna] = valor
        self.tablas[nombre_tabla][indice] = objeto

    def eliminar_fila(self, nombre_tabla, indice):
        del self.tablas[nombre_tabla][indice]

class Usuario():
    global opc_disponible
    global opcion
    def __init__(self, id, nick, tipo, clave, telefono, edad):
        self.id = id
        self.nick = nick
        self.tipo = tipo
        self.clave = clave
        self.telefono = telefono
        self.edad = edad

    # Métodos de la clase Usuarios

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
    
    #Metodo para la creacion de usuarios
    @staticmethod
    def crear_usuario(usuarios):
        id = len(usuarios) + 1 if usuarios else 1
        nick = input("Indique Nick: ")
        tipo = input("Tipo de Usuario (Administrador,Normal,Vendedor): ")
        clave = input("Ingrese clave: ")
        telefono = input("Telefono de contacto: ")
        edad = input("Edad (Solo Numeros): ")
        nuevo_usuario = Usuario(id, nick, tipo, clave, telefono, edad)
        usuarios.append(nuevo_usuario)


#clase normal con menu de la tienda que visualiza un cliente
class Normal(Usuario):
    def menu2(self):
        print("**** Seleccione las siguientes Opciones para navegar: ****")
        print("1)Listar Ofertas 2)Listar todos los productos 3)Administrar su cuenta 4)Salir: ")

    def listar_ofertas(self):
        print("Listando todas las ofertas")

    def listar_productos(self):
        print("Listando todos los productos")

    def admin_cuenta(self):
        print("Seleccion 1)Mostrar NICK 2)Mostrar Clave")
        opcion = int(validacion("12"))
        if opcion == 1:
            usuario_actual.mostrar_nick()
        elif opcion == 2:
            usuario_actual.mostrar_clave()

#clase vendedor con opciones de visualizacion de menu vendedor, esta cuenta hereda de Normal para tener visualizacion de tienda como la ve cliente 
class Vendedor(Normal):
    def menu3(self):
        print("4)Agregar Ofertas 5)Eliminar Ofertas")
        print("6)Realizar Venta 7)Cancelar venta")
        print("8)Salir")

#clase administrador con menu de administrador
class Administrador(Vendedor,BaseDatos):
    def menu1(self):
        print("**** Seleccione las siguientes Opciones para administrar: ****")
        print("1)Menu Usuarios(Ver tienda)  2)Menu Vendedores(Adminiatrar ofertas) 3)Menu Administrador(Modificar Usuarios) 4)Mostrar Nick (Sobreescritura) 5)Salir: ")
    def menu_admin(self):
        print("**** Seleccione las siguientes Opciones para administrar: ****")
        print("1)Nuevo usuario  2)Cambiar Clave Usuario 3)Eliminar Usuario: 4)Actualizar base datos en archivo")
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
            grabar_nuevo.guardar_db(usuarios,productos)


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
    def __init__(self, id_bodega, id_sucursal, sku, stock: int, id_proveedor):
        self.id_bodega = id_bodega
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

    # Métodos de la clase Usuarios

    def mostrar_informacion(self):
        print(f"Informacion de Producto {self.sku} {self.nombre}")


#iniciando las bases de archivo
db_completa = BaseDatos("main.json")
db_cargada = db_completa.cargar_db()
usuarios = db_cargada[0]
productos = db_cargada[1]
for x in productos:
    print(x.nombre)

while True:
    usuario = input("Ingrese su nombre de usuario aquí: ")
    for x in usuarios:
        nombre = x.nick
        usuario_actual = Usuario(x.id,x.nick, x.tipo, x.clave, x.telefono, x.edad)
        if usuario == nombre:      
            usuario_actual.menu()
            if x.tipo == "Administrador":
                while True:
                    usuario_actual = Administrador(x.id,x.nick, x.tipo, x.clave, x.telefono, x.edad)
                    usuario_actual.menu1()
                    opcion = int(validacion("12345"))
                    if opcion == 1:
                        usuario_actual.menu2()
                    elif opcion == 2:
                        usuario_actual.menu2()
                        usuario_actual.menu3()
                    elif opcion == 3:
                        usuario_actual.menu_admin()
                    elif opcion == 4:
                        usuario_actual.mostrar_nick()
                    elif opcion == 5:
                        break
            elif x.tipo == "Normal":
                while True:
                    usuario_actual = Normal(x.id,x.nick, x.tipo, x.clave, x.telefono, x.edad)
                    usuario_actual.menu2()
                    opcion = int(validacion("1234"))
                    if opcion == 1:
                        usuario_actual.listar_ofertas()
                    elif opcion == 2:
                        usuario_actual.listar_productos()
                    elif opcion == 3:
                        usuario_actual.admin_cuenta()
                    elif opcion == 4:
                        break
            elif x.tipo == "Vendedor":
                while True:
                    usuario_actual = Vendedor(x.id,x.nick, x.tipo, x.clave, x.telefono, x.edad)
                    usuario_actual.menu2()
                    usuario_actual.menu3()
                    opcion = int(validacion("12345678"))
                    if opcion == 1:
                        usuario_actual.listar_ofertas()
                    elif opcion == 2:
                        usuario_actual.listar_productos()
                    elif opcion == 3:
                        usuario_actual.admin_cuenta()
                    elif opcion == 8:
                        break