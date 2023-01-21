from random import shuffle
n1 = str(input('[1] Digite um nome: '))
n2 = str(input('[2] Digite um nome: '))
n3 = str(input('[3] Digite um nome: '))
n4 = str(input('[4] Digite um nome: '))
lista = [n1,n2,n3,n4]
shuffle(lista)
print(f'A ordem de apresentação será {lista} ')
