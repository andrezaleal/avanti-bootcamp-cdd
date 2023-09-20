import random

#informar se o usuário é maior de idade baseado na idade que ele fornecer de entrada

idade_str = input("Qual sua idade? ")
idade = int(idade_str)

if(idade>=18):
    print("Você é maior de idade")
else:
    print("Você é menor de idade")

#O usuário tenta adivinhar o numero secreto

numero_secreto = random.randint(1, 100)

numero_str = input("Digite um numero de 1 a 100: ")
numero = int(numero_str)

while(numero != numero_secreto):
    if(numero<numero_secreto):
        print("Pode chutar mais alto..")
        numero_str = input("Digite um numero: ")
        numero = int(numero_str)
    else:
        print("O chute foi muito alto, vamos mirar mais baixo..")
        numero_str = input("Digite um numero: ")
        numero = int(numero_str)
        
print("Parabés, você acertou!!")
    