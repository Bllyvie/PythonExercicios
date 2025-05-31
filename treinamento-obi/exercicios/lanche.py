cod, quant = map(int, input().split())

if cod == 1:
    lan = 4 * quant
    print(f'Total: R$ {lan:.2f}')
     
elif cod == 2:
    lan = 4.50 * quant
    print(f'Total: R$ {lan:.2f}')
    
if cod == 3:
    lan = 5 * quant
    print(f'Total: R$ {lan:.2f}')
    
elif cod == 4:
    lan = 2 * quant
    print(f'Total: R$ {lan:.2f}')
    
elif cod == 5:
    lan = 1.50 * quant
    print(f'Total: R$ {lan:.2f}')
    
