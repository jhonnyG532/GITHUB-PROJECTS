tiene_licencia = input("¿Tienes licencia de conducir? (si/no): ").lower()
esta_sobrio = input("¿Estás sobrio? (si/no): ").lower()

if tiene_licencia == "si" and esta_sobrio == "no":
    print("puedes conducir.")

else:
    print("entregue las llaves")
    
