

def calcular_area_rectangulo(base: float, altura: float) -> float:
    return base * altura

base = float(input("Ingresa la base del rectángulo: "))
altura = float(input("Ingresa la altura del rectángulo: "))

area = calcular_area_rectangulo(base, altura)
print("El área del rectángulo es:", area)




def es_mayor_de_edad(edad: int) -> bool:
    return edad >= 18

edad_usuario = int(input("Ingresa tu edad: "))

if es_mayor_de_edad(edad_usuario):
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")