#Desenvolva um program que leia as duas notas de um aluno, calcule e mostre a sua média
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
M = int(n1 + n2)/2
print('A média do aluno foi {:.1f}'.format(M))