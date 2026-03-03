class CajeroAutomatico:

    def __init__(self):
        self.efectivo_disponible: float = 1000.0

    def solicitar_retiro(self) -> None:
        print("=== Bienvenido al Cajero ===")

        try:
            monto_str: str = input("Ingrese la cantidad a retirar (solo números): ")

            # Convertir a número (si escribe letras, aquí falla y va al except ValueError)
            monto: float = float(monto_str)

            # Si el usuario ingresa 0 o negativo, lanzamos nuestro propio error
            if monto <= 0:
                raise ValueError("No puede retirar cero o valores negativos.")

            # Si no hay suficiente efectivo, lanzamos error
            if monto > self.efectivo_disponible:
                raise ValueError("Fondos insuficientes en el cajero.")

            # Si todo está bien, hacemos el retiro
            self.efectivo_disponible -= monto
            print(f"✅ Retiro exitoso. Quedan ${self.efectivo_disponible} en el cajero.")

        except ValueError as e:
            print(f"⚠️ ERROR: {e}")

        except Exception as e:
            print(f"❌ ERROR CRÍTICO DESCONOCIDO. Contacte soporte. Detalles: {e}")

        finally:
            print("Expulsando tarjeta... Gracias por utilizar nuestro red.\n")


# Prueba
mi_cajero = CajeroAutomatico()
mi_cajero.solicitar_retiro()