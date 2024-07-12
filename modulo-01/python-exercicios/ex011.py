#Faça um programa que leia a largura e altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

L = int(input('Largura: '))
h = int(input('Altura: '))
a = L * h
tinta = a/2
print(f'A área é de {a} \nE será necessário {tinta}L de tinta!')
