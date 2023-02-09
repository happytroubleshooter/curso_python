medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motocicleta")
medios_transporte.sort()
medios_transporte.pop(3)

print(medios_transporte)

frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)

print(frutas)
print(eliminado)


diccionario = {'c1':'valor1','c2':'valor2','c3':'valor3'}
resultado = diccionario['c2']
print(resultado)

cliente = {'nombre':'Juan','apellido':'Fuentes','peso':67.3,'talla':1.76}
consulta = cliente['apellido']
print(consulta)

dic = {'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200,'s3':300}}
print(dic['c3']['s2'])

dic = {'c1':['a','b','c'],'c2':['d','e','f']}
print(dic['c2'][1].upper())

dic = {'a':1,'b':2}
dic['c'] = 3
print(dic)
print(dic.keys())
print(dic.values())

mi_dic = {'nombre':'Karen','apellido':'Jurgens','edad':35,'ocupacion':'Periodista'}
mi_dic['edad'] = 36
mi_dic['ocupacion'] = 'Editora'
mi_dic['pais'] = 'Colombia'
print(mi_dic)

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict['puntos']['points2'][1])

mi_tuple = (1,2,(10,20),4,5)
mi_tuple = list(mi_tuple)
print(mi_tuple)

t = (1,2,3,1)
print(t.index(2))

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tupla)

mi_set1 = set([1,2,3,4,5])
mi_set2 = set([5,6,7,8,9])
mi_set3 = mi_set1.union(mi_set2)
mi_set3.add(0)
mi_set3.remove(9)
mi_set3.discard(0)
mi_set3.pop()
mi_set3.clear()
print(mi_set3)

mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}
mi_set_3 = mi_set_1.union(mi_set_2)
print(mi_set_3)

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.pop()
print(sorteo)

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add("Damián")
print(sorteo)

var1 = 5 >= 2+2
numero = bool(5<6)
list = [1,2,3,4]
control = 5 not in list
print(var1)
print(numero)
print(control)