from pessoa import Pessoa
import json

pessoa = Pessoa()

def calculo_imc():
  return pessoa.peso / pessoa.altura**2

pessoa.altura = float(input('Insira a altura: ')) 
pessoa.peso = float(input('Insira o peso: '))

print('Altura ', pessoa.altura)
print('Peso ', pessoa.peso)
print(f'IMC {calculo_imc()}')
