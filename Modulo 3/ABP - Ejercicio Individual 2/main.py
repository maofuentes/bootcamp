#creacion de la lista 
userclave = "Marcelo, Antonio, Anibal, Pedro, Rodrigo, Jose, Francisca"
#pido el usuario para identificar
usuarios = userclave.split(',')
print(usuarios)
print("Ingrese Usuario")
usuarioingresado = input()

for x in usuarios:
  if (x.lower() == usuarioingresado.lower()):
    print("######################################")
    print("Bienvenido "+x)
    print("######################################")

print("Tenemos los siguientes usuarios registrados:")
print(userclave)