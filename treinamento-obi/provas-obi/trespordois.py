n = int(input())
precos = []
soma = 0

for i in range(n):
    precos.append(int(input()))

precos.sort()
for i in range(n//2):
    if(len(precos) >= 3):
        soma += sum(precos[-2:])
        precos.pop()
        precos.pop()
        precos.pop()
    else:
        soma+= sum(precos)
        break
print(soma)