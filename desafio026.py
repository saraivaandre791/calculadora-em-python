frase = str(input('Digite qualquer frase: ')).strip().lower()
print(f'A letra "a" aparece \033[31m{frase.count("a")}\033[m vezes')
print(f'A letra aparece a primeira vez na posição \033[31m{frase.find("a")+1}\033[m')
print(f'A letra aparece a ultima vez na posição \033[31m{frase.rfind("a")+1}\033[m ')


