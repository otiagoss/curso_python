lista = []
while True:
	print("""
	  1 - Inserir um nome na lista
	  2 - Excluir um nome 
	  3 - Imprimir todos os elemento da lista
	  4 - Sair		
	""")	
	op = int(input('Insira o opção: '))
	if (op == 1):
	  nome = input("Insira um nome: ")
	  lista.append(nome)
	elif (op == 2):
	  nome = input("Insira um nome para remover: ")
	  list.remove(nome)
	elif (op == 3):
	  print(lista)
	elif (op == 4):
	  break
