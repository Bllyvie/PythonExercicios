#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
M = float(input('Qual o valor a ser convertido? '))
cm = M * 100
mm = M * 1000
dm = M * 10
dam = M / 10
hm = M / 100
km = M / 1000
print('A medida de {:.0f}m corresponde a\n {:.0f}cm\n {:.0f}mm\n {:.0f}dm\n {}dam\n {}hm\n {}km\n'.format(M, cm, mm, dm, dam, hm, km))