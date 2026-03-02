#Salida estática: El programa "habla" mostrando texto en pantalla
print("Iniciando el sistema de diagnóstico...")

#Asignación de estado: Guardando valores en la memoria
temperatura_cpu = 45      # Número entero (int)
voltaje = 1.2             # Número decimal (float)
estado_sistema = "Estable"  # Texto (string)

#Recuperación e interpolación de datos
print(f"Estado actual: {estado_sistema}")
print(f"Lecturas: {temperatura_cpu}°C a {voltaje}V")

#Final del programa
print("Diagnóstico finalizado.")