# 02_reto_nomina.py

def calcular_salario_neto(salario_base: float, bonificacion: float = 0.0) -> float:
    # Descuento de salud y pensión (8%)
    descuento: float = salario_base * 0.08
    
    # Calcular salario final
    salario_final: float = salario_base - descuento + bonificacion
    
    return salario_final


# Pedir datos al usuario
salario = float(input("Ingrese el salario base: "))
bono = float(input("Ingrese la bonificación (si no hay, escriba 0): "))

# Llamar la función
salario_neto = calcular_salario_neto(salario, bono)

# Mostrar resultado
print(f"El salario neto es: {salario_neto}")