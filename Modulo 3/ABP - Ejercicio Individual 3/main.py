deportes ={1: "Tiene Afinidad con el Deporte", 2: "Sin Afinidad con el Deporte"}
lugar = {1: "America Latina", 2: "Europa", 3: "Africa", 4: "America del Norte"}
edades = {"1": "18 a 29 Años", "2": "30 y 59 Años", "3": "60 Años y más"}
lista_encuestas = []
    

for x in edades:
    print(x,") ", edades[x])
opcion_edad = input("Seleccion su Rango de Edad: ")
for x in lugar:
    print(x,") ", lugar[x])
opcion_lugar = input("Seleccion su Lugar de Procedencia: ")
for x in deportes:
    print(x,") ", deportes[x])
opcion_deportes = input("Seleccion Afinidad de Deporte: ")

if opcion_edad == "1":
    lista_encuestas.append("Cuestionario de Empleabilidad.")
    if opcion_deportes == "1":
        lista_encuestas.append("Cuestionario de Atletismo.")
elif opcion_edad == "2":
    if opcion_lugar == "1":
        lista_encuestas.append("Cuestionario de Experiencia Laboral.")
    if opcion_deportes == "1":
        lista_encuestas.append("Cuestionario de Atletismo.")
else:
    if opcion_lugar == "1":
        lista_encuestas.append("Cuestionario de Actividades Recreativas.")
        if opcion_deportes == "1":
            lista_encuestas.append("Cuestionario de Natación.")
    
if opcion_deportes == "2":
        lista_encuestas.append("Cuestionario de Deportes en General.")
        
print("Debe responder", str(len(lista_encuestas)), "Cuestionarios, que son los siguientes:")
print(lista_encuestas)
