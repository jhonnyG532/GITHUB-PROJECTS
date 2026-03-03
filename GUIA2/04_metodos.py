class CuentaBancaria:

    def __init__(self, titular: str, saldo_inicial: float):
        self.titular = titular
        self.saldo = saldo_inicial

    # método para depositar dinero
    def depositar(self, cantidad: float) -> None:
        self.saldo += cantidad
        print(f"Depósito exitoso. Nuevo saldo de {self.titular}: ${self.saldo}")

    # método para retirar dinero
    def retirar(self, cantidad: float) -> None:
        if cantidad > self.saldo:
            print(f"Error: {self.titular} no tiene fondos suficientes.")
        else:
            self.saldo -= cantidad
            print(f"Retiro exitoso. Saldo restante: ${self.saldo}")


# Crear una cuenta
cuenta_ana = CuentaBancaria("Ana López", 50000.0)

# Usar los métodos
cuenta_ana.depositar(20000.0)
cuenta_ana.retirar(100000.0)
cuenta_ana.retirar(15000.0)