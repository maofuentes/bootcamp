class Cliente():
    def __init__(self, id_cliente, nombre, apellido, correo, fecha_registro, saldo):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.fecha_registro = fecha_registro
        self.__saldo = saldo

    # Métodos de la clase Cliente:

    def agregar_saldo(self, monto_agregado):
        self.__saldo += monto_agregado
        print(
            f"Usted agrego {monto_agregado} pesos a su cartera digital. Su nuevo saldo es: {self.__saldo}")

    def mostrar_saldo(self):
        print(f"Su saldo actual es: {self.__saldo}")


class Producto():
    def __init__(self, sku, nombre, categoria, proveedor, stock, valor_neto):
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.proveedor = proveedor
        self.stock = stock
        self.valor_neto = valor_neto
        self.__impuesto = 1.19


class Vendedor():
    def __init__(self, run, nombre, apellido, seccion):
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.seccion = seccion
        self.__comision = 0


# Creando las 5 instancias
# Clientes

cliente_1 = Cliente("Rorro", "Rodrigo", "Tuesta",
                    "rodrigo@tuesta.cl", "27-04-2023", 200)
cliente_2 = Cliente("Panchito", "Anibal", "Adalid",
                    "anibal@adalid.com", "27-04-2022", 500)
cliente_3 = Cliente("Freston", "Franco", "Valdes",
                    "franco@valdes.com", "27-04-2023", 0)
cliente_4 = Cliente("Aguila", "Miguel", "Garay",
                    "miguel@garay.com", "24-04-2023", 2000)
cliente_5 = Cliente("Mao", "Marcelo", "Fuentes",
                    "marcelo@fuentes.com", "24-04-2023", 1000000)

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
                opcion_elegida = input("Seleccione una operación: 1) Mostrar saldo 2) Agregar fondos 3) Cerrar sesión: ")
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