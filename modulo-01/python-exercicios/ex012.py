#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
Preco = float(input('Preço do produto: '))
Desc = Preco * 0.05
N_preco = Preco - Desc
print('Seu novo preço é de {:.2f}'.format(N_preco))