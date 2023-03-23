#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, calcule e imprima a soma de todos os números ímpares na lista.
lista = []
lista1 = []
n1 = int(input('Digite o número de elementos que deseja na lista:'))
for i in range(n1):
    numero = int(input('Digite os Números que deseja adicionar na lista:'))
    lista.append(numero)
    if numero % 2 != 0:
        lista1.append(numero)
print(lista)
lista = sum(lista1)
print(lista)