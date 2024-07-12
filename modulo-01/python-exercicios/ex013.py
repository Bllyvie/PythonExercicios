#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, coom 15% de aumento.
Sal = float(input('Antigo salário: '))
N_Sal = Sal * 0.15
Aum = N_Sal + Sal
print('Seu novo salário com 15% de aumento é {:.2f}'.format(Aum))