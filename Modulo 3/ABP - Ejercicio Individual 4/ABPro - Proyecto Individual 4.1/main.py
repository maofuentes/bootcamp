import random
import time
cuestionarios_total = {}
contador_pers = 0
temas = ["Habitos alimenticios", "Experiencia laboral", "Actividades recreativas", "Atletismo", "Natación", "Deportes en general"]

while contador_pers < 7:
    contador = 0
    cuestionarios = {}
    contador_pers = contador_pers+1
    nombre = input("Ingresa tu Nombre:  ")
    print("Los siguientes cuestionarios debera responder:")
    while contador < 5:
        contador = contador+1
        tema = random.choice(temas)
        if tema in cuestionarios:
            tema = random.choice(temas)
        else:   
            cuestionarios.update({tema: nombre})
            cuestionarios_total.update({nombre:cuestionarios})
            #time.sleep(3)
            print(tema," ", end="")
    print("")
    cantidad = len(cuestionarios)
    print(nombre, "Deberá responder: ",cantidad," Cuestionarios")
print("******************************************************************************************************************************")
print("Registro Completo de los 7 Usuarios: ")
print("******************************************************************************************************************************")
print(cuestionarios_total)

