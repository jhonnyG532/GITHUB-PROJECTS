class SistemaSeguridad:

    def __init__(self, pin_acceso: int):
        self.usuario: str = "Admin"  # Público
        self.__pin_secreto: int = pin_acceso
        self.__alarma_activada: bool = True

    # Método para desactivar la alarma
    def desactivar_alarma(self, intento_pin: int) -> None:
        if intento_pin == self.__pin_secreto:
            self.__alarma_activada = False
            print("🔓 Alarma desactivada.")
        else:
            print("🚨 INTRUSO DETECTADO. Llamando a la policía.")


# Crear sistema de seguridad
casa_central = SistemaSeguridad(1234)

# Intentos de desactivar
casa_central.desactivar_alarma(9999)  # PIN incorrecto
casa_central.desactivar_alarma(1234)  # PIN correcto