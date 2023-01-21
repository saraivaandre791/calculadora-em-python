from random import randint
print('\033[34m::\033[m'*20)
n1 = int(input('Tente adivinhar em que numero eu pensei entre 0 e 5: '))
n2 = randint(0, 5)
print(f'\033[33mA maquina escolheu o numero {n2}\033[m')
if n1 == n2:
    print('\033[32mParebens voce acertou o numero escolhido pela maquina!\033[m')
else:
    print('\033[31mVoce errou! Tente novamente.\033[m')





