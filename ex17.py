#Escreva um programa que peça ao usuário para digitar uma lista de nomes e, em seguida, crie uma nova lista que contenha apenas os nomes que contêm a letra "e".
lista = []
lista1 = []
n1 = int(input('Digite o número de nomes que deseja na lista:'))
for i in range(n1):
    nomes = str(input('Digite os Nomes que deseja adicionar na lista:'))
    lista.append(nomes)
    if 'e' in nomes:
        lista1.append(nomes)
print('Lista de nomes:',lista)
print('Lista de nomes que contem a Letra E:', lista1)