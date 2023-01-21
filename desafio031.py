n1 = float(input('Quantos Kms de distancia?: '))
if n1 <= 200:
    print(f'A viagem vai custar R${n1*0.50:.2f}')
else:
    print(f'A viagem vai custar R${n1*0.45:.2f}')



