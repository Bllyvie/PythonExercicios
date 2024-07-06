#No python3 tem a saída formatada onde podemos substituir o bloco print('É um grande prazer te conhecer', nome)
#por print('É um grande prazer te conhecer, {}!'.format(nome)), o nome vai ser formatado para caber dentro de {}
nome = input('Qual é o seu nome?')
print('É um grande prazer te conhecer, {}!'.format(nome))