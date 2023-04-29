import msvcrt
#CODIGO GENERADO SOLO PARA FUNCIONAR EN WINDOWS POR LA BIBLIOTECA EXPORTADA

mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculas = "abcdefghijklmnopqrstuvwxyz"
numeros = "1234567890"
dic_alertas = {"Mayusculas":0, "Minusculas":0,"Numeros":0}

clave = "" 
seguridad = 0

print("Ingrese la contraseña: (Debe tener al menos 3 Mayusculas, 3 Minusculas y 3 Numeros)")
while len(clave) < 9:
    caracteres = (str(msvcrt.getch()))[2]
    clave = clave+caracteres
    if caracteres in mayusculas:
        suma = int(dic_alertas["Mayusculas"])
        dic_alertas["Mayusculas"] = suma+1
        if dic_alertas["Mayusculas"]>2:
            alerta="Cumplido Mayusculas"
            seguridad = seguridad+2
        else:
            alerta="Aun Faltan Mayusculas"
    elif caracteres in minusculas:
        suma = int(dic_alertas["Minusculas"])
        dic_alertas["Minusculas"] = suma+1
        if dic_alertas["Minusculas"]>2:
            alerta="Cumplido Minusculas"
            seguridad = seguridad+2
        else:
            alerta="Aun Faltan Minusculas"
    elif caracteres in numeros:
        suma = int(dic_alertas["Numeros"])
        dic_alertas["Numeros"] = suma+1
        if dic_alertas["Numeros"]>2:
            alerta="Cumplido Numeros"
            seguridad = seguridad+2
        else:
            alerta="Aun Faltan Numeros"
#    print(caracteres, alerta, end="",)
    print(" ## "+caracteres+" ## ", alerta, end="")
print("")
if seguridad < 6:
    print("Su CLAVE ES INSEGURA, VUELVA A INTENTARLO")
else:
    print("Su CLAVE ES SEGURA: ", clave)