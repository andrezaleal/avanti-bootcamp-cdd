#criando e imprimindo uma lista de numeros

numeros = [1,2,3,4,5]
print(numeros)

#Pedir para o usuário digitar um animal e verificar se ele está na tupla 

animais = ("cachorro", "gato","papagaio","porco")

animal_user = input("Digite um animal: ")

if animal_user in animais:
    print("Esse animal está na lista!")
else:
    print("Esse animal não está na lista!")