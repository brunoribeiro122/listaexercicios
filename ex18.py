#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, crie uma nova lista que contenha apenas os números que são divisíveis por 3.
lista = []
lista3 = []
n = int(input('Digite a quantidade de elementos que deseja adicionar na lista:'))
for i in range(n):
    numeros = int(input('Digite o número que deseja adicionar na lista: '))
    lista.append(numeros)
    if numeros % 3 == 0:
        lista3.append(numeros)
print('Lista com Todos os números:',lista)
print('Lista de números divisíveis por 3:',lista3)