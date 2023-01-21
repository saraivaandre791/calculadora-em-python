n1 = float(input('Em qual velocidade esta o carro? Km: '))
if n1 > 80:
    print('\033[31mVoce ultrapassou o limite de velocidade!\033[m')
    print(f'\033[31mMultado no valor de R${(n1-80)*7:.2f}')
else:
    print('\033[32mDentro do limite!')


