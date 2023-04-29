JJVV = [
    {"Nombre": "Sara Teresa Sánchez del Pinar", "Telefono": "939444052", "Casa": 1, "FechaIngreso": "22/01/2023", "edad": "38"},
    {"Nombre": "Valentina Laverde de la Rosa", "Telefono": "944405821", "Casa": 2, "FechaIngreso": "12/01/2023", "edad": "58"},
    {"Nombre": "Oscar de la Renta", "Telefono": "939123052", "Casa": 3, "FechaIngreso": "12/02/2023", "edad": "78"},
    {"Nombre": "Martin Elias de los Rios Acosta", "Telefono": "939111152", "Casa": 4, "FechaIngreso": "12/03/2023", "edad": "28"},
    {"Nombre": "Juan Fernando Perez del Corral", "Telefono": "933333052", "Casa": 5, "FechaIngreso": "12/05/2023", "edad": "18"},
    {"Nombre": "Efrain de las Casas Mejía", "Telefono": "934444452", "Casa": 6, "FechaIngreso": "01/01/2023", "edad": "48"},
    {"Nombre": "Matias de Greiff Rincon", "Telefono": "937777552", "Casa": 7, "FechaIngreso": "03/01/2023", "edad": "58"}
]

for x in JJVV:
    print("****************************************")
    print("Informacion de Socios: ")
    print("Nombre:", x["Nombre"])
    print("Telefono:", x["Telefono"])
    print("Casa:", x["Casa"])
    print("Ingreso:", x["FechaIngreso"])
    print("Edad:", x["edad"])

"""
¿Qué problemas encontró con esta forma de almacenar la información?

Que al almacenar la informacion de esta manera si la desplegamos con .items() la despliega sin poder generar un formato mas ordenado (Despliega como bloque)

"""