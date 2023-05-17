"""
DESARROLLO - Continuación del trabajo.
En base al proyecto que estás desarrollando, identifica al menos seis posibles errores en la ejecución de
su programa. Integre por lo menos IndexError, TypeError, KeyError.
Ejecuta un Finally al final de cada manejo de error. Este debe entregar un mensaje que explique el error
y la forma de solucionarlo.
Describa cual es la utilidad de manejar los errores en la programación.

Envíe el diagrama de Clases desde Object hasta los tipos de errores, tal como se muestra en los videos.
Describa la estructura del diagrama de forma detallada.
"""

opc_disponible = "1"
opcion = 0

def validacion(opc_disponible):
    opcion_ingresada = input()
    while True:
        if opcion_ingresada in opc_disponible:
            return opcion_ingresada
        else:
            print("Opcion Ingresada no valida")
            opcion_ingresada = input()

class Usuario():
    global opc_disponible
    global opcion

    def __init__(self, id, nick, tipo, clave):
        self.id = id
        self.nick = nick
        self.tipo = tipo
        self.clave = clave

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

    def validar_usuario(self):
        try:
            usuario = input("Ingrese su nombre de usuario aquí: ")
            for x in usuarios:
                nombre = x.nick
                usuario_actual = Usuario(x.id, x.nick, x.tipo, x.clave)
                if usuario == nombre:      
                    usuario_actual.menu()
                    if x.tipo == "Administrador":
                        while True:
                            usuario_actual = Administrador(x.id, x.nick, x.tipo, x.clave)
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
                            usuario_actual = Normal(x.id, x.nick, x.tipo, x.clave)
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
                            usuario_actual = Vendedor(x.id, x.nick, x.tipo, x.clave)
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
        #codigos de errores de prueba en este ejemplo no son utilizables (solo en caso de ingreso de datos invalidos)

        except IndexError:
            print("Ocurrió un error de índice. Asegúrese de que los índices utilizados sean válidos.")
        except TypeError:
            print("Ocurrió un error de tipo. Asegúrese de que los tipos de datos utilizados sean correctos.")
        except KeyError:
            print("Ocurrió un error de clave. Asegúrese de que las claves utilizadas sean válidas.")
        except Exception as e:
            print("Ocurrió un error:", e)
        finally:
            print("Datos ingresados")

class Normal(Usuario):
    def __init__(self, id, nick, tipo, clave):
        self.id = id
        self.nick = nick
        self.tipo = tipo
        self.clave = clave
    
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
            self.mostrar_nick()
        elif opcion == 2:
            self.mostrar_clave()

class Vendedor(Normal):
    def menu3(self):
        print("4)Agregar Ofertas 5)Eliminar Ofertas")
        print("6)Realizar Venta 7)Cancelar venta")
        print("8)Salir")

class Administrador(Vendedor):
    def menu1(self):
        print("**** Seleccione las siguientes Opciones para administrar: ****")
        print("1)Menu Usuarios(Ver tienda)  2)Menu Vendedores(Adminiatrar ofertas) 3)Menu Administrador(Modificar Usuarios) 4)Mostrar Nick (Sobreescritura) 5)Salir: ")
    
    def menu_admin(self):
        print("**** Seleccione las siguientes Opciones para administrar: ****")
        print("1)Nuevo usuario  2)Cambiar Clave Usuario 3)Eliminar Usuario: ")

    def mostrar_nick(self):
        print(f"El Nick desde la Vista de Administrador es: {self.nick}")

usuario1 = Administrador(1, "Marcelo", "Administrador", "123123")
usuario2 = Normal(2, "Pedro", "Normal", "123123")
usuario3 = Vendedor(3, "Pablo", "Vendedor", "123123")

usuarios = [usuario1, usuario2, usuario3]

while True:
    Usuario.validar_usuario(usuarios)
