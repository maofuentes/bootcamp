"""
Se solicita como entregable de este Sprint la implementación final de todos los conceptos vistos
durante el Módulo 4: Python avanzado. Por tanto, se debe poner foco en lo siguiente:
Comentar debidamente el código para que sea comprensible por un tercero.
Se solicitan crear las siguientes clases:

● Seleccione cuatro de las clases de su diagrama. Privilegie las clases que tienen algún tipo de
herencia, Debe desarrollarlo en un script, plasmando la dinámica entre clases y respectivas
herencias.
● Identifique y diseñe claramente sus respectivos métodos y atributos. Las clases deben heredar
atributos-métodos utilizando la función super().
● Asegúrese de manejar al menos 2 posibles errores, según los contenidos revisados.
● Privilegie la clase usuario (o equivalente). En este sentido debe almacenar la información de los
usuarios en un archivo JSON o CSV según estimen conveniente.
Recuerde comentar debidamente el código, para facilitar su comprensión.
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


class BaseDatos:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.tablas = {}
        self.cargar_db()

    def cargar_db(self):
        with open(self.nombre_archivo) as archivo_json:
            data = json.load(archivo_json)
            usuarios = [Usuario(u["id"], u["nick"], u["tipo"], u["clave"], u["telefono"], u["edad"]) for u in data["Usuarios"]]
            return usuarios

    def guardar_db(self, usuarios, productos, bodegas, ventas):
        data = {"Usuarios": [], "Productos": [], "Bodegas": [], "Ventas": []}
        for u in usuarios:
            data["Usuarios"].append({"id": u.id, "nick": u.nick, "tipo": u.tipo, "clave": u.clave, "telefono": u.telefono, "edad": u.edad})
        
        with open(self.nombre_archivo, "w") as archivo_json:
            json.dump(data, archivo_json)


#iniciando las bases de archivo
db_completa = BaseDatos("main.json")
db_cargada = db_completa.cargar_db()
usuarios = db_cargada[0]