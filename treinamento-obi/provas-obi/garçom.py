N = int(input())

total_qubrados = 0

for _ in range(0, N):
    L, C = map(int, input().split())
    if L > C:
        total_qubrados = total_qubrados + C
print(total_qubrados)