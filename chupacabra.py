secreta = "chupacabra"

while True:
    inserir = input('Insira a palavra secreta: ')
    if inserir == secreta:
        print("Você saiu do loop com sucesso!")
        break
    else:
        print("Palavra incorreta. Tente novamente.")