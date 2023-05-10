import json
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

data = {}
data["productos"] = []

class Productos():
    global data
    def __init__(self, descuento, nombre, precio, precio_venta, stock, id=False):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.precio_venta = precio_venta
        self.stock = stock
        self.descuento = descuento
    
    def agregar(self):
        #ID automatico
        nuevo_id = len(data["productos"])+1
        nuevo_producto = {"descuento": self.descuento, "nombre": self.nombre, "precio": self.precio, "precio_venta": self.precio_venta, "stock": self.stock, "id": nuevo_id }
        data["productos"].append(nuevo_producto)
    
    def mostrar(self):
        print(data["productos"])

    def eliminar(self):
        pass
    #Modificar producto (Precio,nombre)
    def modificar(self):
        pass

    def modificar_stock(self):
        pass

    def modificar_descuentos(self):
        pass

class Basedatos():
    def __init__(self, basedatos):
        self.basedatos = basedatos
    
    def mostrar(self):
        print(self.basedatos)

    def abrir(self):
        with open(self.basedatos, "r") as archivo:
            data = json.load(archivo)
            return data

    def grabar(self):
        with open(self.basedatos, 'w') as archivo:
            json.dump(data, archivo)
    
    def grabar_copia(self):
        with open(self.basedatos, 'w') as archivo:
            json.dump(data, archivo)

gestiones = Productos(0,"cocacola", 1200, 1500, 10)


while True:
    opcion = int(input("1) Agregar Producto | 2) Mostrar Producto: | 3) Cargar Base de Datos: | 4) Grabar Base de Datos: | 5) Grabar COPIA Base de Datos:  "))
    if opcion == 1:
        gestiones.agregar()
    elif opcion == 2:
        print(data)
    elif opcion == 3:
        DBtrabajo = input("Ingrese nombre DB, por defecto ingrese: data ")+".json"
        gestionesDB = Basedatos(DBtrabajo)
        data = gestionesDB.abrir
        print("Carga Completa de Base de datos")
    elif opcion == 4:
        DBtrabajo = input("Ingrese nombre DB, por defecto ingrese: data ")+".json"
        Basedatos.grabar(DBtrabajo)
    elif opcion == 5:
        DBtrabajo = input("Nombre archivo copia seguridad")+".json"
        Basedatos.grabar_copia(DBtrabajo)
        print("Copia de seguridad grabada con los datos actuales")