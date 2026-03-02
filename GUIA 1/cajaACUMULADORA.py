total_ahorrado = 0
print("iniciando caja acumuladora")
for numero in range(1,4):
    consignacion = float(input(f"ingresa la consignacion numero {numero}: "))
    total_ahorrado += consignacion
print(f"el total ahorrado es: {total_ahorrado}")