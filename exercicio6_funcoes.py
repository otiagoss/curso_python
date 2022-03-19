def procura_nome(lista):
    #if 'Tiago' in lista:
    #    return True      
    for nome in lista:
        if nome == "Tiago":
            return True

lista = ["Tiago","Valeria","Luan","Edgar"]

#if procura_nome(lista):
#    print("Encontrou")

resultado = procura_nome(lista)
if resultado:
    print('Encontrou')
else:
    print('Não achou meu Tiago')
