class Proveedor():
    def __init__(self, id_proveedor, rut, nombre_legal, razon_social, pais, tipo):
        self.id_proveedor = id_proveedor
        self.rut = rut
        self.nombre_legal = nombre_legal
        self.razon_social = razon_social
        self.pais = pais
        self.tipo = tipo

    # Métodos de la clase Cliente:

    def agregar_saldo(self, monto_agregado):
        self.__saldo += monto_agregado
        print(f"Usted agrego {monto_agregado} pesos a su cartera digital. Su nuevo saldo es: {self.__saldo}")

    def mostrar_saldo(self):
        print(f"Su saldo actual es: {self.__saldo}")

proveedor1 = Proveedor(1,15763730,"Marcelo","Comercioquinta","Chile","Nacional")

print(proveedor1.pais)