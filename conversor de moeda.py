"""Programa que leia quanto dinheiro a pessoa tem na carteira
e quantos dolare ela pode comprar."""
from time import sleep
print('-' * 20)

real = float(input('Quanto dinheiro voce tem disponivel? R$'))
cota = float(input('Cotação atual do dolar R$'))
dolar = real / cota
print('-='*35)
print(f'Com \033[32mR${real:.2f}\033[m (reais)...')
sleep(0.5)
print(f'Voce pode comprar \033[31m${dolar:.2f}\033[m (dolares) ')

print('_' * 20)
