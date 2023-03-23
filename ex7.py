#Escreva um programa que peça ao usuário para digitar uma lista de nomes e, em seguida, imprima o nome mais longo e o nome mais curto da lista.
lista = []
n1 = int(input('Digite o número de elementos que deseja na lista:'))
for i in range(n1):
    palavra = str(input('Digite os nomes que deseja adicionar na lista:'))
    lista.append(palavra)
lista1 = max(lista, key=len)
lista2 = min(lista, key=len)
print(lista)
print('Maior nome da lista é:',lista1)
print('Menor nome da lista é:',lista2)
