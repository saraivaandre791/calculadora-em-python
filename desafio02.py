nome = input('Digite seu nome: ')
ano = int(input('Qual sua idade? Digite somente o numero: '))
ano1 = 2023 - ano
print('='*30)
print(f'\033[31m{nome}\033[m \033[32mVoce nasceu em {ano1} certo?\033[m')
print('='*30)

