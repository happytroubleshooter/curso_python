texto = input("ingrese su texto: ").lower()
letras = []

letra1 = letras.append(input("ingrese su primera letra: ").lower())
letra2 = letras.append(input("ingrese su primera segunda: ").lower())
letra3 = letras.append(input("ingrese su primera tercera: ").lower())

print("REPETICION DE LETRAS")

result1 = texto.count(letras[0])
result2 = texto.count(letras[1])
result3 = texto.count(letras[2])

print(f"La letra '{letras[0]}' se repite {result1} veces en su texto")
print(f"La letra '{letras[1]}' se repite {result2} veces en su texto")
print(f"La letra '{letras[2]}' se repite {result3} veces en su texto")

print("CUANTAS PALABRAS HAY")

lista_palabras = texto.split()

print(f"Su texto contiene {len(lista_palabras)} palabras en total")

print("CUAL ES LA PRIMERA Y ULTIMA LETRA")

print(f"La primera letra de su texto es '{texto[0]}', y la ultima es '{texto[-1]}'")

print("ORDEN INVERTIDO DE PALABRAS")

texto_separado = texto.split()
texto_separado.reverse()
texto_invertido = " ".join(texto_separado)

print(f"Su texto, en orden invertido, se lee asi: \n'{texto_invertido}'")

print("BUSCAR 'PYTHON'")

resultado_true = "python" in texto
dic = {True:"SI",False:"NO"}

print(f"La palabra 'python' {dic[resultado_true]} esta en su texto")

