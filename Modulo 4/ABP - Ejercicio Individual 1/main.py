from datetime import date
from itertools import cycle
from random import choice, randint
from string import ascii_letters, digits, punctuation

usuarios = []
administradores = [{"Rut":"157637304"}]

def validacion():
    #Funcion para validar que las opciones digitadas sean correctas
    global opc_disponible
    opcion_ingresada = input()
    while True:
        if opcion_ingresada in opc_disponible:
            return opcion_ingresada 
        else:
            print("Opcion Ingresada no valida")
            opcion_ingresada = input()

class Usuario:
        # un metodo de clase para crear un objeto de clase
        # Persona por año de nacimiento.
    def validar_Edad(rut):
        if int(rut) < 20000000:
            texto = "Mayor de Edad"
        else:
            texto = "Menor de Edad"
        return texto
    # un metodo estatico para revisar el rut de una persona
    def rut(v_rut):
        #valida el largo del rut
        if len(v_rut) > 8 and len(v_rut) <10:
            dv = v_rut[-1]
            if dv.lower() == "k":
                dv = 10
            rut = v_rut.rstrip(v_rut[-1])
            reversed_digits = map(int, reversed(str(rut)))
            factors = cycle(range(2, 8))
            s = sum(d * f for d, f in zip(reversed_digits, factors))
            error = (-s) % 11
            if int(dv) == error:
                return True
            else:
                return False
        else:
            return False
    # un metodo estatico para validar o crear una nueva clave
    def clave(validar):
        if validar == 0:
            # Definir el número mínimo de caracteres:
            largo = 8
            # Definir el rango de letras para el generador de characteres
            letras_disponibles = ascii_letters + digits + punctuation
            # Hace un bucle en el que genera contraseñas y verifica si alguna cumple con los requisitos
            while True:
            # Crea la contraseña de 8 caracteres de una lista de carácteres
                contraseña = "".join(choice(letras_disponibles) for _ in range(largo))
            # Verifica que tenga al menos una mayúscula, una minúscula y un dígito
                if any(char.isupper() for char in contraseña) and any(char.islower() for char in contraseña) and any(char.isdigit() for char in contraseña):
                    break
            # Devuelve la contraseña creada
            return contraseña
        elif validar == 1:
            for x in usuarios:
                if rut == x["Rut"]:
                    if validar_clave == x["Clave"]:
                        print("Usuario Valido")
                    else:
                        print("Usuario y/o Contraseña Invalida")
class Administrador:
    # un metodo para validar usuario
    def ingresar(a_rut):
        for x in administradores:
            if a_rut == x["Rut"]:
                tipo = "Administrador"
                return tipo
            else:
                tipo = "No es Administrador"
                return tipo

    #metodo para eliminar usuarios
    def eliminar():
        print("Eliminando Usuarios")
    #metodo para listar usuarios
    def listar():
        print(usuarios)

class Entradas():
    # un metodo para entregar entradas mayor edad
    def validar(t_edad):
        if t_edad == "Mayor de Edad":
            salida = Entradas.mayor()
            return salida
        else:
            salida = Entradas.menor()
            return salida
    #metodo para entregar entradas menor edad
    def mayor():
        entradas = "Entradas desde las 22:00"
        return entradas
    def menor():
        entradas = "Entradas desde las 16:00 hasta las 21:30"
        return entradas


while True:
    print("*******************************************************************")
    print("************Bienvenido al sistema de Registro para PUB*************")
    print("*******************************************************************")
    print("** 1)Registrarse 2)Obtener Entrada 3)Descuentos 4)Administracion **")
    opc_disponible = "1234"
    opcion = int(validacion())
    if opcion == 1:
        rut = input("Ingrese su RUT sin puntos, guion y/o digito verificador: ")
        validar = Usuario.rut(rut)
        if validar == True:
            print("Rut Valido, ", end="")
            validar_clave = Usuario.clave(0)
            print("Su Nueva contraseña es: ", validar_clave,"guarde en un lugar seguro")
            usuarios.append({"Rut":rut,"Clave":validar_clave})
        else:
            print("Datos falsos")
    elif opcion == 2:
        rut = input("Ingrese su RUT sin puntos, guion y/o digito verificador: ")
        validar = Usuario.rut(rut)
        if validar == True:
            clave = input("Ingrese su clave: ")
            validar_clave = Usuario.clave(1)
            print(Entradas.validar(Usuario.validar_Edad(rut[-1])))
        else:
            print("Rut invalido")
    elif opcion == 3:
        rut = input("Ingrese su RUT sin puntos, guion y/o digito verificador: ")
        validar = Usuario.rut(rut)
        if validar == True:
            print("Su RUT",rut,"tiene disponible los siguientes descuentos: ")
        else:
            print("Rut no valido")
    elif opcion == 4:
        rut = input("Ingrese su RUT sin puntos, guion y/o digito verificador: ")
        validar = Usuario.rut(rut)
        if validar == True:
            clave = input("Ingrese su clave: ")
            validar_clave = Usuario.clave(1)
            
            if Administrador.ingresar(rut) == "Administrador":
                print("Seleccione las Opciones de Administracion")
                print("1)Listar Usuarios 2)Eliminar Usuarios 3)Descuentos")
                opc_disponible = "123"
                opcion = int(validacion())
                if opcion == 1:
                    Administrador.listar()
                elif opcion == 2:
                    Administrador.eliminar()
        else:
            print("Rut invalido")
