from time import sleep
def menu():
    print('-=-' * 15)
    print(f'{'':10} ## Gestão a Vista ##'.upper())
    print('-=-'* 15)
    print('Qual opção o senhor(a) deseja: ')
    sleep(1)
    print('\033[32m[1]\033[m', 'Adicionar Produto.')
    print('\033[34m[2]\033[m', 'Atualizar produto.')
    print('\033[36m[3]\033[m', 'Visualizar Estoque.')
    print('\033[33m[4]\033[m', 'Sair do programa')
