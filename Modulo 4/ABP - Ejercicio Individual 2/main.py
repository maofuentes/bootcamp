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

class Productos:
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

class Basedatos:

    def abrir():
        with open("data.json", "r") as archivo:
            data = json.load(archivo)
            return data

    def grabar(self):
        with open("data.json", 'w') as file:
            json.dump(data, file)

data = Basedatos.abrir()
print(data)
gestiones = Productos(0,"cocacola", 1200, 1500, 10)

while True:
    opcion = int(input("1) Agregar Producto | 2) Mostrar Producto: "))
    if opcion == 1:
        gestiones.agregar()
    elif opcion == 2:
        print(data)