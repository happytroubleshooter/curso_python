texto = input("Ingresa tu texto: ").lower()
l1 = input("Ingresa una letra: ").lower()
l2 = input("Ingresa una letra: ").lower()
l3 = input("Ingresa una letra: ").lower()

# -- Transformar texto -- #

lista_texto = list(texto)

# -- 1. Cuantas veces se repiten las letras -- #
result1 = lista_texto.count(l1)
result2 = lista_texto.count(l2)
result3 = lista_texto.count(l3)

print(f"La letra \"{l1}\" se repite {result1} cantidad de veces")
print(f"La letra \"{l2}\" se repite {result2} cantidad de veces")
print(f"La letra \"{l3}\" se repite {result3} cantidad de veces")

# -- 2. Cuantas palabras hay en total -- #

lista = texto.split()
result4 = len(lista)
print(f"Tu texto tiene {result4} palabras en total")

# -- 3. Cual es la primera y ultima letra -- #

print(f"La primera letra de tu texto es \"{texto[0]}\", y la ultima es \"{texto[-1]}\".")

# -- 4. Palabras en orden inverso -- #

lista.reverse()
invertidas = " ".join(lista)
print(f"Asi es como se veria tu texto con sus palabras invertidas:\n\"{invertidas.capitalize()}\"")

# -- 5. Si la palabra "python" se encuentra dentro del texto -- #

result5 = "python" in texto
if result5 is True: print(f"La palabra \"Python\" esta en el texto")
if result5 is False: print(f"La palabra \"Python\" no esta en el texto")
