prova = float(input())
trabalho = float(input())
media = (prova + trabalho) / 2
if(media >= 6):
    print("aprovado",media)
if(media >= 2 and media < 6):
    print("talvez com a sub",media)
if(media < 2):
    print("reprovado")
