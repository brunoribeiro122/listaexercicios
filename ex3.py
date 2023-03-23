
#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, encontre o número máximo e o número mínimo da lista.
lista = []
n1 = int(input('Digite o número de elementos que deseja na lista:'))
for i in range(n1):
    numero = int(input('Digite os Números que deseja adicionar na lista:'))
    lista.append(numero)
lista.sort()
print(lista)
print('Número minimo da lista é:',lista[0])
print('Número maximo da lista é:',lista[-1])
