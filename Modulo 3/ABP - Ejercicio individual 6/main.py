import sys
import time

datos = []
contador = 0 
opcion = 0

def validar():
    global contador, opcion, usuario, clave
    usuario = input("Ingrese Usuario: ")
    if usuario == "salir":
        print(datos)
        sys. exit()
    else:
        usuario = usuario.lower().strip()
        clave = input("Ingrese su contraseña: ")
        opcion = 1


while contador == 0:
    validar()
    if opcion == 1:
        edad = input("Ingrese su edad(Con numeros): ")
        while True:
            if edad.isdigit():
                nuevo = {"usuario":usuario,"password":clave,"edad":edad}
                print(usuario)
                print(edad)
                time.sleep(5)
                print(clave)
                datos.append(nuevo)
                break
            else:
                edad = input("Ingresó letras, por favor vuelve a ingresar la edad: ")

