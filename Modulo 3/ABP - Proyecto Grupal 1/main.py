#Listado de objetos

# inventario = {"Guitarra": 500000, "Bajo": 600000, "Trompeta": 350000, "Batería": 1300000, "Teclado": 800000}

#Valor del inventario
valor_guitarra = 500000
valor_bajo = 600000
valor_trompeta = 350000
valor_bateria = 1300000
valor_teclado = 800000

#Venta de guitarras
print("¿Cuántas guitarras se han vendido?: ")
numero_guitarras = input()
total_guitarra = int(numero_guitarras)*valor_guitarra
print("El total de la compra es: " + str(total_guitarra) + " pesos.")

#Venta de bajos
print("¿Cuántas bajos se han vendido?: ")
numero_bajo = input()
total_bajo = int(numero_bajo)*valor_bajo
print("El total de la compra es: " + str(total_bajo) + " pesos.")

#Venta de trompetas
print("¿Cuántos bajos se han vendido?: ")
numero_trompeta = input()
total_trompeta = int(numero_trompeta)*valor_trompeta
print("El total de la compra es: " + str(total_trompeta) + " pesos.")

#Venta de baterías
print("¿Cuántas baterías se han vendido?: ")
numero_baterías = input()
total_batería = int(numero_baterías)*valor_bateria
print("El total de la compra es: " + str(total_batería) + " pesos.")

#Venta de teclados
print("¿Cuántos teclados se han vendido?: ")
numero_teclados = input()
total_teclado = int(numero_teclados)*valor_teclado
print("El total de la compra es: " + str(total_teclado) + " pesos.")

#Total de la compra

total_ventas = (total_guitarra+total_bajo+total_batería+total_teclado+valor_trompeta)
iva_ventas = total_ventas*0.19
neto_ventas = total_ventas - iva_ventas
print("El valor total de todas las ventas es: " + str(total_ventas) + " pesos.")
print("El valor neto de la compar es: " + str(neto_ventas) + " pesos.")
print("El IVA de esta compra es: " + str(iva_ventas) + " pesos.")