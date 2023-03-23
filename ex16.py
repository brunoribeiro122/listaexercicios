#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, crie uma nova lista que contenha apenas os números que aparecem mais de uma vez na lista original.
lista1 = []
lista = []
listarepetidos = []
n = int(input('Digite a quantidade de elementos que deseja adicionar na lista: '))
for i in range(n):
    numeros = int(input('Digite o número que deseja adicionar na lista: '))
    lista1.append(numeros)
    if numeros not in lista:
        lista.append(numeros)
    else:
        listarepetidos.append(numeros)
print(lista1)
print('A lista de números que apareceram mais de uma vez é',listarepetidos)