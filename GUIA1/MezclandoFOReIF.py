print("filtro de seguridad")
edades_acceso = [15,22,17,30,14]
for edad in edades_acceso:
    if edad >= 18:
        print(f"acceso concedido a la edad de {edad}")
    else:
        print(f"acceso denegado a la edad de {edad}")
