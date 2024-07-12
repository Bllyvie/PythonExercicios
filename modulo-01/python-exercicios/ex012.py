#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Preço do produto: '))
desc = preco * 0.05
N_preco = preco - desc
print('Seu novo preço é de {:.2f}'.format(N_preco))