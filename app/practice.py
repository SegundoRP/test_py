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


print(True and True)
print(True and False)
print(True or False)

BOOLEAN = True

if BOOLEAN:
    print('inside condition')
# elif
# else

CONTADOR = 5

while CONTADOR <=10:
    print('CONTADOR vale', CONTADOR)

    if CONTADOR == 5:
        print('rompe CONTADOR')
        break

    CONTADOR += 1


lista = ['palabra1', 'palabra3']

for palabra in lista:
    if palabra == 'palabra2':
        print('palabra encontrada')
        break
else:
    print('palabra no encontrada')

for number in range(1, 10):
    # Last number is not in the range
    print(number)


def my_method(*args):
    print(args)
    # args is a tuple

my_method(1,2,3,4) # (1,2,3,4)

def my_method2(**kwargs):
    print(kwargs)
    # kwargs is a dictionary

my_method2(a= 1, b= 2, c= 3, d= 4) # {'a': 1,'b': 2, 'c': 3, 'd': 4}
