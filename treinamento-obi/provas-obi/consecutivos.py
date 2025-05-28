N = int(input())
V = list(map(int, input().split()))

maior_seq = 1
seq_atual = 1

for i in range (1, N):
    if V [i] == V[i - 1]:
        seq_atual += 1
    
    else:
        seq_atual = 1
    if seq_atual > maior_seq:
        maior_seq = seq_atual
        
print(maior_seq)