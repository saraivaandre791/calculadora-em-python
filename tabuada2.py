"""Refaça o desafio da 'tabuada' mostrando a tabuda de um numero que o usuario
escolher, so que agora utilizando um laço 'for'.
"""
print('\033[32m=\033[m'*15)
num = int(input('Digite um numero: '))
for c in range(1, 21):
    resul = c * num
    print(f'{c}X  \033[32m{num}\033[m  = {resul}')
print('\033[32m='*15)







