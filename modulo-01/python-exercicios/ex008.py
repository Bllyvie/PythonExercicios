#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
M = float(input('Qual o valor a ser convertido? '))
cm = 100 * M
mm = 1000 * M
print('O valor em centímetros é de {} \nE em milímetros é de {}'.format(cm, mm))