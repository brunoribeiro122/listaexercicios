#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima a lista ordenada em ordem decrescente.
lista = []
n1 = int(input('Digite o número de elementos que deseja na lista:'))
for i in range(n1):
    numero = int(input('Digite os Números que deseja adicionar na lista:'))
    lista.append(numero)
lista.sort(reverse = True)
print(lista)