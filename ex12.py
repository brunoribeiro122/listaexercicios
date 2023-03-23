#Escreva um programa que peça ao usuário para digitar uma lista de nomes e, em seguida, verifique se um determinado nome está na lista. Se estiver, imprima "O nome está na lista"; caso contrário, imprima "O nome não está na lista".
lista = []
lista1 = []
n1 = int(input('Digite o número de nomes que deseja na lista:'))
for i in range(n1):
    nomes = str(input('Digite os Nomes que deseja adicionar na lista:'))
    lista.append(nomes)
verificarnome = str(input('Digite o nome que deseja verificar se esta na lista'))
if verificarnome in lista:
    print('O nome',verificarnome,'esta na lista')
else:
    print('O nome',verificarnome,'não esta na lista')
