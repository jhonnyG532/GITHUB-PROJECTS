# 1. CLASE PADRE (Superclase)
class Empleado:
    def __init__(self, nombre: str, salario: float):
        self.nombre: str = nombre
        self.salario: float = salario

    def trabajar(self) -> None:
        print(f"{self.nombre} está cumpliendo su horario regular.")


# 2. CLASE HIJO (Subclase) - Hereda de Empleado
class Desarrollador(Empleado):
    def programar(self) -> None:
        print(f"{self.nombre} está escribiendo código Python.")


# 3. CLASE HIJO CON POLIMORFISMO (Sobrescribe un método)
class Gerente(Empleado):
    def trabajar(self) -> None:
        print(f"{self.nombre} está en una reunión estratégica.")


# Pruebas
dev = Desarrollador("Carlos", 3500.0)
jefe = Gerente("Ana", 6000.0)

dev.trabajar()     # usa el método del Padre (Empleado)
dev.programar()    # usa su método propio (Desarrollador)

jefe.trabajar()    # usa su método sobrescrito (Gerente)