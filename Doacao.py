vic = 2.5
doacao = 0
soma_doacoes = 0
soma_vic = 0
while doacao != -1:
    doacao = float(input())
    
    if doacao != -1:
        soma_doacoes += doacao
        soma_vic = soma_doacoes * vic
        
print(f'VC$ {soma_doacoes:.2f}')
print(f'R$ {soma_vic:.2f}')