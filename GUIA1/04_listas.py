inventario_frutas = ["Manzana", "Pera", "Mango", "Banano"]
print(f"La primera fruta es: {inventario_frutas[0]}")
print(f"La segunda fruta es: {inventario_frutas[1]}")
print(f"La tercera fruta es: {inventario_frutas[2]}")
print(f"La cuarta fruta es: {inventario_frutas[3]}")
print("--- Imprimiendo viñetas automáticas ---")
for fruta in inventario_frutas:
    print(f"- {fruta} disponible en bodega.")