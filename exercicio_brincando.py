pares, impares = [], [] 

num = int(input('Digite o número '))

for i in range(num):
	if (i % 2) == 0:
		pares.append(i)
	else:
		impares.append(i)

print(f' Números pares : {pares}')
print(f' São {len(pares)} números pares')
print(f' Números pares : {impares}')
print(f' São {len(impares)} números impares')