# Escribir un programa que pregunte al usuario la fecha de su nacimiento en
# formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar
# el programa anterior para que también funcione cuando el día o el mes se
# introduzcan con un solo carácter.
fecha = input("Fecha de nacimiento en formato dd/mm/aaaa: ")
día = fecha[:fecha.find("/")]
mes_año = fecha[fecha.find("/")+1:]
mes = mes_año[:mes_año.find("/")]
año = mes_año[mes_año.find("/")+1:]
print("Día", día)
print("Mes", mes)
print("Año", año)