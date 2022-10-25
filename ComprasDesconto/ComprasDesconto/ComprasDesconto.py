Preco_Mercadoria = float(input())
Quantidade_Mercadoria = int(input())
ValorFinal = Preco_Mercadoria * Quantidade_Mercadoria
Desconto = (Quantidade_Mercadoria / 100)
Desconto1 = ValorFinal * Desconto
Desconto2 = (ValorFinal * 0.90) - Desconto1
print(f"{ValorFinal:.2f}")
print(f"{Desconto2:.2f}")