equipo = ("VIVIANA", "FRANCO", "MIGUEL", "MARCELO")
#Crear frase motivadora
frase = "Vamos Viviana, Franco, Miguel y Marcelo, que podemos sacar 7 en todo este bootcamp"
print("La Frase Motivadora: " +str(frase))
#Frase en mayusculas
frase = frase.upper()
frase = frase.replace(",","")
print("En Mayuscula sin comas: " +str(frase))
#transformar a una lista
lista = frase.split()
tupla = tuple(lista)
print("En Formato Lista: "+str(lista))
#en que indice esta cada nombre
for clave in equipo:
    print(clave+" Se encuentra en el index: "+str(lista.index(clave)))
print("La frase Tiene " +str(len(lista))+" Palabras")
print("Imprimir tupla:" +str(tupla))
respuesta = input("¿Quieres incluir tu propio mensaje motivador? (Contesta S o N): ")
mensaje = ""
if respuesta == "S":
    mensaje = input("Escribe Mensaje a continuacion: ")
    print("Tu mensaje es: " +str(mensaje))
else:
    print("Gracias por participar.")

""" 
- Discutan ¿Qué es un dato booleano? ¿Qué utilidad puede tener para el desarrollo de un
programa?
- Investigar qué significa que python sea un lenguaje de tipado dinámico.
- Investigar y documentar sobre la creación de Módulos en Python.
- Investigar y documentar sobre la creación de Paquetes en Python.
- Investigar e implementar el uso del archivo __init__.py

"""