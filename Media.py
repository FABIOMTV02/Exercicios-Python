prova = float(input("Digite a nota da prova: "))
trabalho = float(input("Digite a nota do trabalho: "))
media = (prova + trabalho) / 2
if(media >= 6):
    print("Você foi aprovado e sua média é",media)
if(media >= 2):
    print("Voce precisa de uma recuperação:",media)
    trabalho = float(input("Digite o valor da prova de recuperação: "))
    media = (prova + trabalho) / 2
    #print("Sua nova média é:",media)
if(media < 2):
    print("Infelizmente você foi reprovado e sua nota foi de",media)    
if(media >= 6):
    print("Você foi aprovado e sua nota final foi de:", media)
if(media < 6):
    print("Você foi reprovado e sua nota final foi de:", media)