n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))
if n1 > n2 and n3:
    print(f'O numero \033[31m{n1}\033[m é o maior.')
elif n2 > n3 and n1:
    print(f'O numero \033[31m{n2}\033[m é o maior.')
else:
    print(f'O numero \033[31m{n3}\033[m é o maior.')
