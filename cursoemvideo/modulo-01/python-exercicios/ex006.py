#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
n1 = int(input('Digite um valor: '))
D = n1 * 2
T = n1 * 3
Rq = n1 ** (1/2)
print('O dobro do número é {} \nO triplo é {} \nE a raiz quadrada é {:.2f}'.format(D, T, Rq))