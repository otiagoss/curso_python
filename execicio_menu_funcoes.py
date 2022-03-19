lista = []

def inserir_produto():
    prod = input('Inserir o produto: ')    
    lista.append(prod)


def excluir_produto():
    prod = input('Excluir o produto: ')    
    if prod in lista:
      lista.remove(prod)
    else:
      print(f'{prod} não existe na lista')


def listar_produto():
    print(f'Produtos {lista}')


while True:
    menu = """     
1 - Inserir um produto
2 - Excluir um produto 
3 - Listar os produtos 
4 - Sair		
"""
    print(menu)
    op = int(input('Escolha a opção: '))

    if op == 1:
        inserir_produto()
    elif op == 2:
        excluir_produto()
    elif op == 3:
        listar_produto()
    elif op == 4:
        break
    else:
      print('Opção invalida')
