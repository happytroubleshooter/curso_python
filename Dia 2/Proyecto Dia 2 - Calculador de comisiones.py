nombre = input("cual es tu nombre?: ")
ventas = input("indica cuales fueron tus ventas mensuales totales: ")

ventas = float(ventas)
comisiones = round(ventas*13/100,2)

print(f"Felicitaciones {nombre}! Tus comisiones mensuales son de ${comisiones}")