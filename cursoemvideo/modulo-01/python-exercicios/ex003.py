#Crie um programa que leia dois números e mostre a soma entre eles.
n1 = input('Primeiro número: ')
n2 = input('Segundo número: ')
s = n1 + n2
print('A soma é', s)
print('Tivemos um erro na soma, por favor insira novamente os números')
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
s = n1 + n2
#print('A soma entre',n1, 'e', n2, 'vale', (s))
print('A soma entre {} e {} vale {}'.format(n1, n2, s))