#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima apenas os números pares da lista.
lista = []
listapar = []
n1 = int(input('Digite o número de elementos que deseja na lista:'))
for i in range(n1):
    n = int(input('Digite um número para adicionar na lista'))
    lista.append(n)
    if n % 2 == 0:
        listapar.append(n)
print(lista)
print(listapar)
    
    