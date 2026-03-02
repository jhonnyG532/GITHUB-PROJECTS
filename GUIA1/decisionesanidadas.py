print("diagnostico de red")
hay_internet = input("¿el modem tiene luces encendidas? (si/no): ").lower()

if hay_internet == "si":
    print("el equipo recibe energia")
    luz_roja = input("¿la luz roja esta encendida? (si/no): ").lower()
    if luz_roja == "si":
        print("fallo detectafo, problema en la fibra optica")
    else:
        print("todo normal: su conexion esta lista")
else:
    print("fallo critico, el equipo no recibe energia")
