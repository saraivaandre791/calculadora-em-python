matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for l in range(0, 4):
    for c in range(0, 4):
        matriz[l][c] = int(input(f'Digite um valor: '))
print('-=' * 30)
for l in range(0, 4):
    for c in range(0, 4):
        print(f'{matriz[l][c]}', end='')
    print()





