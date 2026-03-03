class MascotaVirtual:

    # Constructor
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.energia = 10

    # Método jugar
    def jugar(self) -> None:
        self.energia -= 3
        print(f"{self.nombre} jugó. Energía actual: {self.energia}")

    # Método dormir
    def dormir(self) -> None:
        self.energia += 5
        print(f"{self.nombre} durmió. Energía actual: {self.energia}")


# Crear mascota
mascota = MascotaVirtual("Firulais")

# Usar los métodos
mascota.jugar()
mascota.dormir()