#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, crie uma nova lista que contenha apenas os números que são divisíveis por um número fornecido pelo usuário.
lista = []
lista2 = []
n = int(input('Digite o número de elementos que deseja adicionar na lista:'))
divisor = int(input('Digite o número divisor que deseja utilizar:'))
for i in range(n):
    numeros = int(input('Digite o número que deseja adicionar na lista: '))
    lista.append(numeros)
    if numeros % divisor == 0:
        lista2.append(numeros)
print('Lista completa:', lista)
print('Lista com os números divisíveis por',divisor,':',lista2)
