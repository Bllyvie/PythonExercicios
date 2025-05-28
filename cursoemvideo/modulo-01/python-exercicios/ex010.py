#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere US$1,00 = R$5,43
real = float(input('Qual o valor? '))
dolar = real / 5.43
print('Você poderá comprar U${:.2f} doláres'.format(dolar))