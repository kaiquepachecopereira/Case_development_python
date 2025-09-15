import sys
sys.path.append('./python/main_funcoes.py')
import main_funcoes
from time import sleep

#Programa Principal
main_funcoes.menu()

optionlist = [1, 2, 3, 4] #Condição do Loop# 
inicio = 0
estoque = {}

while (inicio not in optionlist): 
    escolha = int(input('Digite a Opção de (1-4): '))
    print('\033[0;31;40mAguarde....\033[m')
    sleep(1)

    if escolha == 1:
         nome_produto = input(f'Digite nome do produto: ')
         preco_produto = float(input('Digite o Valor do produto:R$ ').upper())
         qtd_produto = int(input('Digite a quantidade do produto: '))
         estoque[nome_produto] = {'preço': preco_produto}, {'Quantidade': qtd_produto}
         print(f'\033[0;32;40m{nome_produto} Adicionado com sucesso!\033[m')
    elif escolha == 2:
        produto_atualizar = input('Digite o nome do produto para atualizar: ')
        if produto_atualizar in estoque:
            preco_produto = float(input('Digite o novo preço do produto: '))
            quantidade_produto = int(input('Digite a nova quantidade em estoque: '))
            estoque[produto_atualizar] = {'Preço': preco_produto}, {'Quantidade': quantidade_produto}
            print('\033[0;32;40mDados atualizados com sucesso!\033[m')
        else:
            print('Produto não encontrado. Verifique o nome do produto')
    elif escolha == 3:
        for i in estoque.items():
           print(i)
        
    elif escolha == 4:
        print('Saindo do Programa!')
        inicio = 4
    else:
       print("Opção Inválida!\nTente Novamente.")
    sleep(1)  
       