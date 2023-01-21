from time import sleep
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')

com = nome.replace(" ","")
pri = nome.split()
sleep(2)
print(f'Em maiusculo: \033[33m{nome.upper()}\033[m')
print(f'Em minusculo: \033[33m{nome.lower()}\033[m')
print(f'O nome tem \033[33m{len(com)}\033[m letras')
print(f'O primeiro nome tem \033[33m{len(pri[0])}\033[m letras')






