"""
DESARROLLO - Continuación del trabajo.
Como parte de este ejercicio se necesita crear clases utilizando sintaxis de Python, para comprender
las ventajas de la programación orientada a objetos.
En vista a nuestro sistema desarrollado anteriormente se solicita lo siguiente:
Agregar una nueva clase pertinente a la aplicación que están desarrollando e identificar en ella al
menos cuatro atributos (uno de ellos debe ser opcional). Agréguela al diagrama intuitivo que realizó en
la actividad anterior.

Se deberá crear métodos para cada uno de los usuarios. Piensen en diferentes acciones particulares
que pueda ejecutar cada una de sus clases. Desarrolle cuatro métodos por cada clase. Dos deben
incluir acciones que afecten números y dos que afecten strings. Al menos uno de estos métodos debe
aplicar los contenidos de ‘sobrecarga de métodos’.
También se solicita que existan condiciones para realizar las validaciones correspondientes.
"""

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

class Usuario():
    def __init__(self, id, nick, tipo, clave):
        self.id = id
        self.nick = nick
        self.tipo = tipo
        self.clave = clave

    # Métodos de la clase Usuarios

    def mostrar_nick(self):
        print(f"El Nick del Usuario es: {self.nick}")

    def mostrar_tipo(self):
        print(f"El Usuario tiene privilegios: {self.tipo}")

    def mostrar_id(self):
        print(f"La id de usuario es: {self.id}")
    
    def mostrar_clave(self):
        print(f"La clave de usuario es: {self.clave}")

class Mod_Usuario():
    def __init__(self, id, nick, tipo, clave):
        self.id = id
        self.nick = nick
        self.tipo = tipo
        self.clave = clave

    # Métodos de la clase Usuarios

    def modificar_nick(self):
        nuevonick = input("Indique nuevo Nick: ")
        return nuevonick

    def modificar_id(self):
        nuevoid = input("Indique nuevo ID(Solo numeros): ")
        if nuevoid.isdigit():
            return nuevoid

    def modificar_clave(self):
        nuevoclave = input("Indique nueva clave: ")
        return nuevoclave
    
    def modificar_tipo(self):
        nuevotipo = input("Indique nuevo tipo (Usuario o Administrador): ")
        while True:
            if nuevotipo == "Administrador" or "Usuario":
                return nuevotipo
        
    def modificar_nickyclave(self, *nickyclave):
        x.clave = nickyclave[1]
        x.nick = nickyclave[0]

usuario1 = Usuario("1","marcelo","Administrador","123123")
usuario2 = Usuario("2","miguel","Usuario","123123")

lista_usuarios = [usuario1, usuario2]

while True:
    print("*************************************************************************")
    print("**********BIENVENIDO A PANEL DE GESTION DE USUARIOS**********************")
    usuario = input("Ingrese su nombre de usuario aquí: ")
    for x in lista_usuarios:
        nombre = x.nick
        if usuario == nombre:
            usuario_actual = x
            id_actual = x.id
            print("      Seleccione 1) Mostrar datos Usuarios 2) Modificar Usuario          ")
            opc_disponible = "12"
            opcion = int(validacion())
            if opcion == 1:
                print("Seleccione 1)Mostrar id 2)Mostrar Nick 3)Mostrar clave 4)Mostrar Privilegios")
                opc_disponible = "1234"
                opcion = int(validacion())
                if opcion == 1:
                    usuario_actual.mostrar_id()
                elif opcion == 2:
                    usuario_actual.mostrar_nick()
                elif opcion == 3:
                    usuario_actual.mostrar_clave()
                elif opcion == 4:
                    usuario_actual.mostrar_tipo()
            elif opcion == 2:
                for x in lista_usuarios:
                    if x.id == id_actual:
                        print("Seleccione 1)Modificar id 2)Modificar Nick 3)Modificar clave 4)Modificar Privilegios 5)Modificar Nick y Clave")
                        opc_disponible = "12345"
                        opcion = int(validacion())
                        if opcion == 1:
                            nuevo_id = Mod_Usuario.modificar_id("")
                            x.id = nuevo_id
                        elif opcion == 2:
                            nuevo_nick = Mod_Usuario.modificar_nick("")
                            x.nick = nuevo_nick
                        elif opcion == 3:
                            nuevo_clave = Mod_Usuario.modificar_clave("")
                            x.clave = nuevo_clave
                        elif opcion == 4:
                            nuevo_tipo = Mod_Usuario.modificar_tipo("")
                            x.tipo = nuevo_tipo
                        elif opcion == 5:
                            mod_user = Mod_Usuario(x.id,x.nick,x.tipo,x.clave)
                            nuevo_nick = input("Ingrese nuevo Nick: ")
                            nuevo_clave = input("Ingrese nueva Clave: ")
                            mod_user.modificar_nickyclave(nuevo_nick,nuevo_clave)
    else:
        print("ALERTA: Usuario Invalido")