#Escreva um programa que peça ao usuário para digitar uma lista de palavras e, em seguida, imprima apenas as palavras que começam com a letra "a".
lista = []
listaA = []
n1 = int(input('Digite o número de elementos que deseja na lista:'))
for i in range(n1):
    palavra = (input('Digite um palavra que deseja adicionar na lista'))
    lista.append(palavra)
    if palavra[0] == 'a' or palavra[0] == 'A':
        listaA.append(palavra)
print(lista)
print(listaA)