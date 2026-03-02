#edad

edad_usuario = int(input("Por favor, ingresa tu edad en números: "))

# 2. Evaluación lógica
print("Evaluando permisos de acceso...")

# 3. Bifurcación (If / Elif / Else)
if edad_usuario >= 18:
    print(" Acceso concedido: Eres mayor de edad.")

elif edad_usuario >= 13:
    print("Acceso restringido: Eres adolescente, necesitas permiso de un tutor.")

else:
    print("Acceso denegado: Eres menor de edad.")

# 4. Esta línea se ejecuta siempre
print("Gracias por usar el sistema.")