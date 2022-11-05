trabalho = float(input())
prova = float(input())
media = (prova + trabalho) / 2
if(media >= 6):
    print("aprovado")
else:    
    if(((trabalho + 10)/2) >= 6):
        print("talvez com a sub")
    else:
        print("reprovado")
