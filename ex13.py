#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, encontre e imprima o segundo número mais alto na lista.
lista = []
n = int(input('Digite a quantidade de elementos que deseja adicionar na lista: '))
for i in range(n):
    numeros = int(input('Digite o número que deseja adicionar na lista: '))
    lista.append(numeros)
lista.sort(reverse = True)
print('O segundo número mais alto da lista é:',lista[1])

