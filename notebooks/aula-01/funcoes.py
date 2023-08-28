#função de saudação recebendo um nome como parametro

def saudacao(nome):
    print("Seja bem vinda "+nome)

saudacao("Rute")

#funcao apra saber de um numero é primo

def numeroPrimo(numero):

    if numero <= 1:
        print(f"O número {numero} não é primo.")
        return

    for i in range(2, numero):
        if numero % i == 0:
            print(f"O número {numero} não é primo.")
            return
    
    print(f"O número {numero} é primo.")


numeroPrimo(8)
        