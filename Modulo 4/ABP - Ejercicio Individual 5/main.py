"""Incorporar un archivo CSV el cual se encargará de almacenar información de los colaboradores de tu
aplicación en un archivo externo.
En un script diferente será posible acceder al archivo y verificar la información de teléfono y edad.

Así mismo se solicita contar con un registro de los usuarios de tu aplicación. Este registro debe contar
con información del nombre, nombre de usuario, un identificador y la contraseña. Este registro debe ser
serializado. Identifiquen la forma de desarrollarlo.
En un script diferente, acceda a los diferentes datos registrados.
Guarde información de 10 colaboradores y 10 usuarios.
"""
import csv

opc_disponible = "1"
opcion = 0

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

#clase para mostrar datos de Propio de cada usuario ya sean Usuarios Normales, Administradores o vendedores
class Archivo():
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
    #metodo para carga de usuarios desde archivo csv
    def cargar_usuarios(self):
        with open(self.nombre_archivo, newline='') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            usuarios = []
            for fila in lector_csv:
                id, nick, tipo, clave, telefono, edad = fila
                usuarios.append(Usuario(int(id), nick, tipo, clave, telefono, int(edad)))
            return usuarios
    #metodo para grabar usuarios en usuarios
    def guardar_usuarios(self, usuarios):
        with open(self.nombre_archivo, 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            for usuario in usuarios:
                escritor_csv.writerow([usuario.id, usuario.nick, usuario.tipo, usuario.clave, usuario.telefono, usuario.edad])

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
    def crear_usuario(usuarios):
        id = usuarios[-1].id + 1 if usuarios else 1
        nick = input("Indique Nick: ")
        tipo = input("Tipo de Usuario (Administrador,Normal,Vendedor): ")
        clave = input("Ingrese clave: ")
        telefono = input("Telefono de contacto: ")
        edad = input("Edad (Solo Numeros): ")
        usuarios.append(Usuario(int(id), nick, tipo, clave, telefono, int(edad)))


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
class Administrador(Vendedor,Archivo):
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
            grabar_nuevo = Archivo("usuarios.csv")
            grabar_nuevo.guardar_usuarios(usuarios)

#sobre escribir metodo
    def mostrar_nick(self):
        print(f"El Nick desde la Vista de Administrador es: {self.nick}")

#Clase de gestion de Archivo


usuarios = Archivo('usuarios.csv')
usuarios = usuarios.cargar_usuarios()

while True:
    usuario = input("Ingrese su nombre de usuario aquí: ")
    for x in usuarios:
        nombre = x.nick
        usuario_actual = Usuario(x.id, x.nick, x.tipo, x.clave, x.telefono, x.edad)
        if usuario == nombre:      
            usuario_actual.menu()
            if x.tipo == "Administrador":
                while True:
                    usuario_actual = Administrador(x.id, x.nick, x.tipo, x.clave, x.telefono, x.edad)
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
                    usuario_actual = Normal(x.id, x.nick, x.tipo, x.clave, x.telefono, x.edad)
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
                    usuario_actual = Vendedor(x.id, x.nick, x.tipo, x.clave, x.telefono, x.edad)
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