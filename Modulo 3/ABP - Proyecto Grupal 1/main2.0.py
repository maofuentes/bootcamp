inventario = {"Guitarra": 500000, "Bajo": 600000, "Trompeta": 350000, "Batería": 1300000, "Teclado": 800000}
total = 0

for clave in inventario:
    print("Ingrese cantidad de:"+clave)
    cantidad = input()
    total = total+inventario[clave]*int(cantidad)

iva_ventas = total*0.19
neto_ventas = total - iva_ventas
print("El valor total de todas las ventas es: " + str(total) + " pesos.")
print("El valor neto de la compar es: " + str(neto_ventas) + " pesos.")
print("El IVA de esta compra es: " + str(iva_ventas)+" pesos.")