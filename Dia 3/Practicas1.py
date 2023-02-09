texto = input("texto: ").lower()

ver = "python" in texto
dic = {True:"SI",False:"NO"}

print(f"La palabra 'python' {dic[ver]} esta en el texto")