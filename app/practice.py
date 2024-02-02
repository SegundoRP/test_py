# tupla
tupla = (1, 2, 3)
# inmutable
print(tupla[0])
print(tupla)

# lista
lista = [1, 2, 3]
print(lista[1])
lista.append(4)
print(lista)

# conjunto
conjunto1 = {1, 2, 3, 4, 2, 3}
conjunto2 = {0, 2, 4, 2, 9}
# cant repeat members
print(conjunto1 | conjunto2) # union
print(conjunto1 & conjunto2) # intersection
print(conjunto1 - conjunto2) # differences between a respect to b
print(conjunto1 ^ conjunto2) # values not repeat between members

# diccionario
diccionario = {'clave1': 1, 'clave2': 2}
print(diccionario['clave1'])
diccionario.pop('clave1')
print(diccionario)
