from math import sin, cos, tan, radians
an = float(input('Digite o valor do angulo: '))
sen = sin(radians(an))
cos = cos(radians(an))
tang = tan(radians(an))
print(f'O  angulo de {an} tem o seno de {sen:.2f}')
print(f'O  angulo de {an} tem cosseno de {cos:.2f}')
print(f'O  angulo de {an} tangente de {tang:.2f}')


