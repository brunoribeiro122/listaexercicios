#Escreva um programa que peça ao usuário para digitar uma lista de palavras e, em seguida, crie uma nova lista que contenha apenas as palavras que têm um número ímpar de letras.
lista = []
lista1 = []
n = int(input('Digite o número de elementos que deseja adicionar na lista: '))
for i in range(n):
    palavras = (input('Digite a palavra que deseja adicionar na lista: '))
    lista.append(palavras)
    nLetras = len(palavras)
    print(nLetras)
    if nLetras % 3 == 0:
        lista1.append(palavras)
print(lista)
print('lista de palavras que contem um número ímpar de letras ', lista1)
        