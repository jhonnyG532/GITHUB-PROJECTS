# 03_reto_acumulador.py

# Creamos la variable acumuladora
total_compra = 0

print("🧾 Bienvenido a la caja registradora")

# Bucle que se repite exactamente 5 veces
for numero in range(1, 6):
    precio = float(input(f"Ingrese el precio del producto {numero}: "))
    total_compra += precio

# Mostrar el total final
print(f"💰 El costo total de la compra es: ${total_compra}")