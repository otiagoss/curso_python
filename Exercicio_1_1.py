codigo, qtde, vlrUnitario = [], [], []
valorTotal = 0
for i in range(2):
  codigo.append(int(input('Digite o código da peça: ')))
  qtde.append(int(input('Digite a quantidade da peça: ')))
  vlrUnitario.append(float(input('Digite o valor unitário: ')))	
  valorTotal += (qtde[i] * vlrUnitario[i])

print(f'VALOR A PAGAR; R$ {valorTotal}')
	  