from builtins import len, print, input, any


def num_there(nome):
    return any(i.isdigit() for i in nome)


nome = input('Digite seu nome: ')
tamanho = len(nome)

if num_there(nome) == True :
    print('Nome inválido. Favor inserir apenas letras.')
    print()
    nome = input('Digite seu nome novamente: ')
    tamanho = len(nome)

if tamanho <= 4:
    print(f' Olá {nome}, seu nome é curto!')

elif tamanho <= 6:
    print(f'Olá {nome}, seu nome é normal...')

elif tamanho > 6:
    print(f'Olá {nome}, seu nome é muito grande!')

else:
    pass

