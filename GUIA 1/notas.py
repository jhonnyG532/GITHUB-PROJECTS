nota_estudiante = int(input("Ingresa la nota del estudiante: "))

if nota_estudiante >= 101:
    print("Nota inválida")

elif nota_estudiante >= 60:
    print("Aprobado")

else:
    print("Reprobado")