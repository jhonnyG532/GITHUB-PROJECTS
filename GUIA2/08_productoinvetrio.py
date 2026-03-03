
class Producto:
    def __init__(self, nombre: str, precio: float, stock: int):
        self.nombre: str = nombre
        self.precio: float = precio
        self.stock: int = stock

    def vender(self, cantidad: int) -> None:
        """
        Intenta vender una cantidad del producto.
        Si la cantidad pedida es mayor al stock, lanza ValueError y lo maneja sin colapsar.
        """
        try:
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser mayor que 0.")

            if cantidad > self.stock:
                raise ValueError("Stock insuficiente")

            # Si todo está bien, se descuenta del stock
            self.stock -= cantidad
            total: float = self.precio * cantidad
            print(f"✅ Venta exitosa: {cantidad} x {self.nombre} = ${total}. Stock restante: {self.stock}")

        except ValueError as e:
            print(f"⚠️ Venta fallida ({self.nombre}): {e}. Stock actual: {self.stock}")



class ProductoPerecedero(Producto):
    def __init__(self, nombre: str, precio: float, stock: int, dias_vencimiento: int):
        super().__init__(nombre, precio, stock)  # llama al constructor del padre
        self.dias_vencimiento: int = dias_vencimiento




arroz = Producto("Arroz", 3500.0, 10)
leche = ProductoPerecedero("Leche", 4200.0, 5, 7)

print("=== INVENTARIO INICIAL ===")
print(f"{arroz.nombre} | precio: ${arroz.precio} | stock: {arroz.stock}")
print(f"{leche.nombre} | precio: ${leche.precio} | stock: {leche.stock} | vence en: {leche.dias_vencimiento} días")

print("\n=== VENTAS ===")
arroz.vender(3)     # exitosa
arroz.vender(20)    # falla por stock
leche.vender(2)     # exitosa
leche.vender(10)    # falla por stock
leche.vender(0)     # falla por cantidad inválida