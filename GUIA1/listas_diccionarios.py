estudiantes = [
    {"nombre": "jhonny", "nota": 80},
    {"nombre": "maria", "nota": 90},
]
for persona in estudiantes:
    if persona["nota"] >= 60:
        print("el estudiante", persona["nombre"], "aprobo")