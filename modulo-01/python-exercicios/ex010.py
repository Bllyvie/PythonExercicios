#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere US$1,00 = R$3,27

Real = float(input('Qual o valor? '))
Dolar = Real * 3.27
print('Você poderá comprar U${} doláres'.format(Dolar))