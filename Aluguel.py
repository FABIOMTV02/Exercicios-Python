valor_divida = int(input())
valor_pagamento = int(input())

pagamento = 0

while valor_divida != 0:
    if valor_divida >= valor_pagamento:
        antes = valor_divida
        valor_divida = valor_divida - valor_pagamento
        depois = valor_divida
    else:
        antes = valor_divida
        valor_divida = valor_divida - valor_divida
        depois = valor_divida
    pagamento += 1
    
    print(f'pagamento: {pagamento}')
    print(f'antes = {antes}')
    print(f'depois = {depois}')
    print('-----')