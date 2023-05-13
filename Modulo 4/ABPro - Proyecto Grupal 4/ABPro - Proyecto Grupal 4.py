class PersonaNatural(Usuario):

    """Clase abstracta para todas las personas naturales. Hereda de la clase Usuario."""

    def __innit__(self, id_usuario: str, contraseña: str, correo: str, nombre: str, apellido: str):
        super().__innit__(id_usuario, contraseña, correo)
        self.nombre = nombre
        self.apellido = apellido


class PersonaJuridica(Usuario):

    """Clase abstracta para todos las personas jurídicas que trabajen con la empresa."""

    def __innit__(self, id_usuario: str, contraseña: str, correo: str, razon_social: str, rut):
        super().__innit__(id_usuario, contraseña, correo)
        self.razon_social = razon_social
        self.rut = rut


class Cliente(PersonaNatural):

    """Clase abstracta para todos los clientes de la tienda. Agrega las variables: saldo, fecha_registro y VIP."""

    # Variables de clase:
    carro_compras = {}  # Se ingresa Producto:unidades

    def __init__(self, id_usuario, contraseña, nombre: str, apellido: str, correo: str, fecha_registro, saldo: int, vip=False):
        super().__innit__(id_usuario, contraseña, correo, nombre, apellido)
        self.fecha_registro = fecha_registro
        self.__saldo = saldo
        self.vip = vip

    # Métodos de la clase Cliente:
    
    # Métodos para el saldo:

    def agregar_saldo(self, monto_agregado):
        """Agrega el monto ingresado en el parámetro a _saldo"""
        self.__saldo += monto_agregado
        print(
            f"Usted agrego {monto_agregado} pesos a su cartera digital. Su nuevo saldo es: {self.__saldo}")

    def mostrar_saldo(self):
        print(f"Su saldo actual es: {self.__saldo}")

    def descontar_saldo(self, monto_deducido):
        """Descuenta el monto ingresado en el parámetro como argumento a la variable _saldo."""
        self.__saldo -= monto_deducido

    def get_saldo(self):
        return self.__saldo
    
    # Métodos para el carro de compras:
    
    def añadir_carro(self, **productos):
        """Agrega al carro de compras los productos ingresados como diccionario producto:unidades."""
        self.carro_compras.update(productos)

    def limpiar_carro(self):
        """Limpia el carrito de compras del usuario."""
        self.carro_compras.clear()





class Vendedor(PersonaNatural):

    """Clase para todos los vendedores de la tienda. Añade las variables: comisión, run, sección y promoción."""

    # Variables de la clase:

    comision = 0
    promocion = False

    def __innit__(self, id_usuario: str, contraseña: str, correo: str, nombre: str, apellido: str, seccion: str, run, cargo: str):
        super().__innit__(id_usuario, contraseña, correo, nombre, apellido)
        self.seccion = seccion
        self.run = run
        self.seccion = seccion

    
    #Métodos de la clase

    def procesar_carro(self, Cliente):
        """Hace la transacción de todos los carritos de un producto con la acción de vender."""
        for producto in Cliente.carro_compras:
            self.vender(producto, Cliente.carro_compras[producto], Cliente)

    def vender(self, Producto, unidades, Cliente):
        """Descuenta las unidades del inventario del producto, 
        calcula una comisión de 0.5% oara el vendedor y descuenta el valor total de la compra al saldo del cliente. 
        Arroja un mensaje si el saldo o las unidades de la transacción son insuficientes para satisfacer la compra. """

        valor_final = Producto.valor_neto * unidades
        if valor_final <= Cliente.get_saldo() and unidades <= Producto.stock:
            comision += Producto.valor_neto * 0.005 * unidades
            Producto.stock -= unidades
            Cliente.descontar_saldo(valor_final)
            print(
                f"Se compró {unidades} unidad(es) del producto {Producto.nombre} por un valor de {valor_final}")
        elif valor_final > Cliente.get_saldo():
            print("El cliente tiene saldo insuficiente para esta compra.")
        elif unidades > Producto.stock:
            print("No hay suficientes unidades del producto para realizar la compra.")

    def reiniciar_comision(self):
        """Reinicia el contador de comisión del vendedor."""
        self.comision = 0





class Proveedor(PersonaJuridica):

    """Clase para los proveedores constituidos como personas jurídicas."""
    def __innit__(self, id_usuario: str, contraseña: str, correo: str, razon_social: str, rut, pais):
        super().__innit__(id_usuario, contraseña, correo, razon_social, rut)
        self.pais = pais


class Proveedor(PersonaNatural):

    """Clase para los proveedores que son personas naturales."""
    def __innit__(self, id_usuario: str, contraseña: str, correo: str, nombre: str, apellido: str):
        return super().__innit__(id_usuario, contraseña, correo, nombre, apellido)







# Creando las 5 instancias
# Clientes

cliente_1 = Cliente("Rorro", "Rodrigo", "Tuesta", "rodrigo@tuesta.cl", "27-04-2023", 200)
cliente_2 = Cliente("Panchito", "Anibal", "Adalid", "anibal@adalid.com", "27-04-2022", 500)
cliente_3 = Cliente("Freston", "Franco", "Valdes", "franco@valdes.com", "27-04-2023", 0)
cliente_4 = Cliente("Aguila", "Miguel", "Garay", "miguel@garay.com", "24-04-2023", 2000)
cliente_5 = Cliente("Mao", "Marcelo", "Fuentes", "marcelo@fuentes.com", "24-04-2023", 1000000)

# Lista que contiene todos los clientes
lista_clientes = [cliente_1, cliente_2, cliente_3, cliente_4, cliente_5]

# Productos

producto_1 = Producto("01", "Panchito a lo pobre",
                      "Panchos", "Argentina", 100, 2500)
producto_2 = Producto("02", "Panchito catalán", "Panchos", "España", 100, 3000)
producto_3 = Producto("03", "Panchito italiano",
                      "Panchos", "Italia", 100, 2000)
producto_4 = Producto("04", "Panchito mediterráneo",
                      "Panchos", "Grecia", 100, 5000)
producto_5 = Producto("05", "Panchito americano", "Panchos", "USA", 100, 3500)

# Vendedores

vendedor_1 = Vendedor("Vivi", "Viviana", "Vera", "Programación")
vendedor_2 = Vendedor("Profesor X", "Carlos", "Javier", "Mutante")
vendedor_3 = Vendedor("Mythrandil", "Gandalf",
                      "El Sabio", "Magia y hechicería")
vendedor_4 = Vendedor("Portador del anillo único", "Frodo",
                      "Bolsón", "La comunidad del anillo")
vendedor_5 = Vendedor("Pececillo", "Felipe", "Avello", "Humor")

# Ejecución

while True:
    print("Bienvenido a Te lo compro.")
    # Búsqueda del usuario en la lista de clientes
    usuario = input("Ingrese su nombre de usuario aquí: ")
    for instance in lista_clientes:
        nombre = instance.nombre
        if usuario == nombre:
            while True:
                # Elección de método
                opcion_elegida = input(
                    "Seleccione una operación: 1) Mostrar saldo 2) Agregar fondos 3) Cerrar sesión: ")
                if opcion_elegida == "1":
                    instance.mostrar_saldo()
                    break
                elif opcion_elegida == "2":
                    monto = int(input("Ingrese el monto a depositar:"))
                    instance.agregar_saldo(monto)
                    break
                elif opcion_elegida == "3":
                    break
                else:
                    print("La opción ingresada no fue reconocida, vuelva a intentarlo.")
    salir = input("¿Desea realizar otra operación? (S/N): ")
    if salir.lower() == "n":
        break
