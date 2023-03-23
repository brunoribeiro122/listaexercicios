#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, remova todos os números duplicados da lista e imprima a nova lista
lista = []
lista2 = []
n = int(input('Digite o número de elementos que deseja adicionar na lista: '))
for i in range(n):
    numeros = int(input('Digite o número que deseja adicionar na lista: '))
    lista.append(numeros)
    if numeros not in lista2:
        lista2.append(numeros)
print(lista)
print('Lista sem números duplicados é',lista2)