import random
import time

productos = {"Producto1": 120, "Producto2": 150}
stock_proveedor = 150
contador = 0

while True:
    if contador == 10:
        print("Inventario: ",productos)
        contador = 0
    else:
        producto_e = random.choice([clave for clave in productos.keys()])
        cantidad_e = int(random.randint(1,10))
        cantidad_d = int(productos[producto_e])
        cantidad_t = cantidad_d-cantidad_e
        productos.update({producto_e: cantidad_t})
        contador = contador+1
        print("Se vendió",cantidad_e,"De:",producto_e)
        time.sleep(3)
        if cantidad_t <= 100 and stock_proveedor > 0:
            productos.update({producto_e: cantidad_t+50})
            print("Proveedor agregó 50 items de", producto_e )
            stock_proveedor = stock_proveedor-50
        elif cantidad_t <= 100 and stock_proveedor == 0:
            print("Proveedor quedó sin stock de reserva")
        
        

