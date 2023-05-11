from random import choice, randint
from string import ascii_letters, digits, punctuation
"""
SPRINT DE ENTREGA:
Se solicita como entregable de este Sprint la implementación final de todos los conceptos vistos
durante el Módulo 1 de Python básico. Por tanto, se debe poner foco en lo siguiente:
● Elaborar un programa que recorra una lista con los nombres de 10 de sus futuros usuarios de tu
aplicación (pueden ser personas, pacientes, organizaciones sociales o instituciones públicas).
● Mediante una función, a todos los usuarios se les creará una cuenta automáticamente.
● Asigne una contraseña para cada cuenta. La contraseña debe ser creada con random y debe
cumplir con los siguientes criterios: mayúsculas, minúsculas y números.
● Cada cuenta debe guardarse en una nueva variable con su respectiva contraseña.
● Por cada cuenta debe pedir un número telefónico para contactarse.

● El programa no terminará de preguntar por los números hasta que todas las organizaciones
tengan un número de contacto asignado.
● El programa debe verificar que el número telefónico tenga 8 dígitos numéricos.
● Se debe guardar como un string.
A modo de entrega, se debe disponer un documento Word o PDF en el que se indique:
- Ruta del repositorio en GitHub

Consideraciones adicionales
- El código debe estar debidamente indentado
- El formato del documento Word queda a criterio del equipo.

"""

usuarios = [
    {"id": 1, "nombre": "Miguel Garay Gallardo"},
    {"id": 2, "nombre": "Franco Valdés Navarro"},
    {"id": 3, "nombre": "Viviana Vera Ceballos"},
    {"id": 4, "nombre": "Marcelo Lagos Perez"},
    {"id": 5, "nombre": "Olivia Norambuena Johnson"},
    {"id": 6, "nombre": "Francisco Sinatra Olivares"},
    {"id": 7, "nombre": "Orlando Borquez Diaz"},
    {"id": 8, "nombre": "Nicolás Ríos Gonzalez"},
    {"id": 9, "nombre": "Ivania Salas Sierra"},
    {"id": 10, "nombre": "Rosalia Garate López"}
]

# FUNCIONES

# Funcion de gestion y creacion de cuentas de usuario
# Franco: Cambié la función para que acepte la lista que desea ordenar y no esté definida dentro del alcance de la misma.


def gestion_usuario(lista_usuarios):
    # se avanza por la lista de usuarios
    for dic_usuario in lista_usuarios:

        # Crea las variables para el nombre de usuario, la contraseña y el ingreso de un número telefónico
        # Asigna los valores de las variables llamando a las funciones correspondientes
        nombre_usuario = dic_usuario["nombre"]
        usuario = creador_usuario(dic_usuario)
        contraseña = creador_contraseña()
        telefono = numero_telefonico(nombre_usuario)

        # Actualizando los diccionarios
        dic_usuario.update({
            "usuario": usuario,
            "contraseña": contraseña,
            "teléfono": telefono
        })


def creador_usuario(diccionario_usuario):
    # se toma el nombre completo
    parte1 = diccionario_usuario["nombre"]
    # se separa por los espacios
    palabras = parte1.split()
    # se crea una cadena vacia
    nueva_cadena = ""
    # se recorre esa cadena
    for letra in palabras:
        # se toma la inicial y se une al id de usuario
        nueva_cadena = nueva_cadena + letra[0] + str(diccionario_usuario["id"])
    return nueva_cadena


def creador_contraseña():
    # Definir el número mínimo de caracteres:
    largo = 8

    # Definir el rango de letras para el generador de characteres

    letras_disponibles = ascii_letters + digits + punctuation

    # Hace un bucle en el que genera contraseñas y verifica si alguna cumple con los requisitos
    while True:

        # Crea la contraseña de 8 caracteres de una lista de carácteres
        contraseña = "".join(choice(letras_disponibles) for _ in range(largo))

        # Verifica que tenga al menos una mayúscula, una minúscula y un dígito
        if any(char.isupper() for char in contraseña) \
                and any(char.islower() for char in contraseña) \
                and any(char.isdigit() for char in contraseña):
            break

    # Devuelve la contraseña creada
    return contraseña


def asignador_contraseñas(lista_usuarios):
    # Itera sobre la lista de usuarios y les otorga una contraseña al llamar a la función creador_contraseña

    for persona in lista_usuarios:
        contraseña = creador_contraseña()
        persona.update({"contraseña": contraseña})


def impresion_lista(lista):
    for diccionario in lista:
        for key in diccionario:
            if key == "id":
                print(f"{key}: {diccionario[key]}")
            else:
                print(f"    {key}: {diccionario[key]}")


def numero_telefonico(nombre_usuario):
    telefono = input("Ingrese el número telefónico para " +
                     nombre_usuario + ": ")
    while len(telefono) != 8 or not telefono.isnumeric():
        print("El número telefónico debe tener 8 DIGITOS (numeros). Inténtelo nuevamente.")
        telefono = input("Ingrese el número nuevamente: ")
    return telefono


# EJECUCIÓN

print("Bienvenidos a Programa de gestion de Usuarios v2")

# Agregando los nombres de usuarios
gestion_usuario(usuarios)

# Asignando contraseñas de manera aleatoria de acuerdo con los requerimientos
asignador_contraseñas(usuarios)

# Imprimiendo la información de la lista de usuarios con un formato agradable
impresion_lista(usuarios)
