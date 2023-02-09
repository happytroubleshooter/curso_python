texto = input("Ingresa tu texto aqui: ").lower()
letras = []

texto_list = texto.split()

letras.append(input("Ingresa tu primera letra: ").lower())
letras.append(input("Ingresa tu segunda letra: ").lower())
letras.append(input("Ingresa tu tercer letra: ").lower())

print("CONTAR LETRAS")

print(f"La letra '{letras[0]}' aparece {texto.count(letras[0])} cantidad de veces")
print(f"La letra '{letras[1]}' aparece {texto.count(letras[1])} cantidad de veces")
print(f"La letra '{letras[2]}' aparece {texto.count(letras[2])} cantidad de veces")

print("")