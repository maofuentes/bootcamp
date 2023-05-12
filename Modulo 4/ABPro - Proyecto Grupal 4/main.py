class Usuario():

    """Clase abstracta para todos los usuarios de la plataforma. Posee elementos comunes heredables a clases como Cliente o vendedor."""

    def __innit__(self, id_usuario: str, contraseña: str, correo: str):
        self.id_usuario = id_usuario
        self.__contraseña = contraseña
        self.correo = correo

    def __set_contraseña(self, nueva_contraseña):
        self.__contraseña = nueva_contraseña

    def __get_contraseña(self):
        return self.__contraseña


class Producto():

    """Clase para todos los productos de la tienda."""
    impuesto = 1.19

    def __init__(self, sku, nombre: str, categoria: str, stock: int, valor_neto: int, descuento=1):
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.proveedor = Proveedor
        self.stock = stock
        self.valor_neto = valor_neto
        self.descuento = descuento

    # Métodos de la clase
    
    # Métodos para los descuentos

    def aplicar_descuento(self):
        """Devuelve el valor neto del producto con el descuento ingresado en la instancia."""
        precio_descuento = self.valor_neto * self.descuento
        return precio_descuento

    def actualizar_descuento(self, nuevo_descuento):
        """Actualiza el descuento que puede aplicar sobre el producto. El descuento es un factor que se multiplica por el valor neto.
        Por ejemplo, un 10% de descuento equivale a valor_neto * 0.9."""
        self.descuento = nuevo_descuento

    # Métodos para calcular los valores asociados:

    def valor_bruto(self):
        """Devuelve el valor bruto del objeto sin el IVA aplicado al valor neto."""
        valor_bruto = self.valor_neto / self.impuesto
        return valor_bruto

    def valor_impuesto(self):
        """Devuelve el detalle del impuesto."""
        valor_impuesto = self.valor_neto * (self.impuesto - 1)
        return valor_impuesto
    
class Proveedor():
    def __init__(self, rut, nombre_legal, razon_social, pais, persona):
        self.rut = rut
        self.nombre_legal = nombre_legal
        self.razon_social = razon_social
        self.pais = pais
        self.persona = persona


class Sucursal():

    """Clase para todas las sucursales de venta de la empresa."""
    def __init__(self, stock):
        self.stock = stock

    def reponer_stock(self):
        """Aumenta en 300 unidades el stock de la instancia."""
        self.stock += 300
    
    def gestionar_stock(self, Bodega):
        """Verifica que hayan menos de 50 unidades en stock, después intenta pedir a una instancia de la clase Bodega
        que envía 300 unidades de su inventario. Si la Bodega efectivamente puede hacer esa operación, devuelve True y continua
        y se llama a la función self.reponer_stock(). De lo contrario, devuelve False e imprime un mensaje indicando la 
        falta de inventario de la Bodega."""
        if self.stock < 50:
            if Bodega.descontar_stock():
                self.reponer_stock()
            else:
                print(f"La bodega {Bodega} no cuenta con suficiente inventario para reponer las unidades solicitadas.")

class Bodega():

    """Clase para todas las bodegas de la tienda."""
    def __init__(self, stock):
        self.stock = stock

    def descontar_stock(self):
        if self.stock >= 300:
            self.stock -= 300
            return True
        else:
            print(
                "No queda suficiente unidades en el inventario para reponer el producto.")
            return False

class OrdenCompra():

    """Clase para emitir ordenes de compra de los clientes."""

    valor_despacho = 5000

    def __init__(self, id_ordencompra, producto, despacho: bool):
        self.id_ordencompra = id_ordencompra
        self.producto = producto
        self.depacho = despacho

    def valor_total(self):
        """Devuelve el valor total de la compra. Incluye el valor del evío si aplica."""
        valor_neto = self.producto.valor_neto
        valor_total = valor_neto

        if self.despacho:
            valor_total += self.valor_despacho

        return valor_total

    def detalle_compra(self):
        """Desglosa el valor total en valor bruto del producto, IVA y envío."""
        valor_bruto = self.producto.valor_bruto()
        valor_impuesto = self.producto.valor_impuesto()
        valor_total = self.valor_total()
        if self.despacho:
            print(
                f"""Detalle de la compra:
                    Valor bruto:        {valor_bruto}
                    IVA:                {valor_impuesto}
                    Valor del despacho: {self.valor_despacho}
                    Valor total:        {valor_total}"""
            )
        else:
            print(
                f"""Detalle de la compra:
                    Valor bruto:        {valor_bruto}
                    IVA:                {valor_impuesto}
                    Valor total:        {valor_total}"""
            )
