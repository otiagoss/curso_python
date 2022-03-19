altura = float(input("Insira sua altura: "))

peso = float(input("Insira seu peso: "))

imc = peso / altura**2

msg = '';

if imc < 18.5:
	msg = 'Abaixo do peso'	
	
elif 18.5 >= imc <= 24.9:
	msg = 'peso normal'

elif 25.0 >= imc <= 29.9: 
	msg = 'sobrepeso'

elif 30.0 >= imc <= 39.9:
	msg = 'obesidade 2'

else:
	msg = 'obesidade grave'

print(f'Classificação: {msg} - O IMC é {imc}')
