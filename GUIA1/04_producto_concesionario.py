
# 1. Crear una lista vacía llamada concesionario
concesionario = []

# 2. Crear un bucle for que se repita exactamente 3 veces
for i in range(3):
    # 3. Pedir al usuario la marca, el modelo y el precio
    marca = input("Ingrese la marca del carro: ")
    modelo = input("Ingrese el modelo del carro: ")
    precio = input("Ingrese el precio del carro: ")

    # 4. Empaquetar los datos en un diccionario temporal
    carro = {
        "marca": marca,
        "modelo": modelo,
        "precio": precio
    }

    # 5. Guardar el diccionario dentro de la lista concesionario
    concesionario.append(carro)

# 6. Recorrer la lista e imprimir un informe limpio
print("\n--- INFORME DE VEHICULOS REGISTRADOS ---")
for vehiculo in concesionario:
    print(f"Vehículo registrado: Marca {vehiculo['marca']}, Modelo {vehiculo['modelo']}, Precio: ${vehiculo['precio']}")