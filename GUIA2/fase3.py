# Crear la clase
class Vehiculo:

    # Constructor
    def __init__(self, marca: str, modelo: str, anio: int):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio


# Crear dos objetos
vehiculo1 = Vehiculo("Toyota", "Corolla", 2022)
vehiculo2 = Vehiculo("Mazda", "CX5", 2021)


# Imprimir sus datos
print(f"Vehículo 1: {vehiculo1.marca} {vehiculo1.modelo} {vehiculo1.anio}")
print(f"Vehículo 2: {vehiculo2.marca} {vehiculo2.modelo} {vehiculo2.anio}")