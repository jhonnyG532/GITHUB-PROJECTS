carrito_de_compras = ["Leche", "Pan", "Huevos"]
print(f"El carrito tiene {len(carrito_de_compras)} productos.")

# 1. Agregar un producto
carrito_de_compras.append("Queso")
print(f"Ahora hay {len(carrito_de_compras)} productos.")

# 2. Eliminar el primer producto (Leche)
carrito_de_compras.pop(0)
print(f"El primer producto ahora es: {carrito_de_compras[0]}")
