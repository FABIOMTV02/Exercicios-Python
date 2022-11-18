velocidade = float(input("Digite a velocidade: "))
multa = (velocidade - 80)
if(velocidade > 80):
    print("Você passou a",velocidade, "km/h e foi multado!!!")
    print("E o valor da sua multa é de:",multa * 7.00)
else:
    print("Você passou dentro limite...")
