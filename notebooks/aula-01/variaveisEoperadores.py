import math

# soma, subtração, multiplicação e divisão de inteiros

a = 50
b= 30
soma = a+b
subtacao = a-b
multiplicacao = a*b
divisao = a/b

print(f"soma: {soma}, subtração {subtacao}, mutiliplicação {multiplicacao} e divisão: {round(divisao,1)}")

#area de um circulo solicitando o valor ao usuario 

raio_str = input("Digiteo valor do raio: ")
raio = int(raio_str)
pi = math.pi

areaCirculo = pi*(raio**2)

print(f"Area do circulo {round(areaCirculo,1)}")
