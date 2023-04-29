#creacion de la lista 
userclave = ["Marcelo", "Antonio","Anibal", "Pedro", "Rodrigo", "Jose", "Francisca"]
#pido el usuario para identificar
print("Ingrese Usuario")
usuarioingresado = input()

for x in userclave:
  if (x.lower() == usuarioingresado.lower()):
    print("######################################")
    print("Bienvenido "+x)
    print("######################################")

print("Tenemos los siguientes usuarios registrados:")
print(userclave)