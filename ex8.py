#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima apenas os números que são maiores do que 10.
lista = []
maior10 = []
n1 = int(input('Digite o número de elementos que deseja na lista:'))
for i in range(n1):
    numero = int(input('Digite os Números que deseja adicionar na lista:'))
    lista.append(numero)
    if numero > 10:
        maior10.append(numero)
print(lista)
print('Os números maiores que 10 são:',maior10)