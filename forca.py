def jogar():
    print("***********************************")
    print("****Bem-vindo ao jogo da Forca!****")
    print("***********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False
    # enquanto o usuario nao enforcou=false e nao acertou=false vamos jogar
    while(not enforcou and not acertou):

        chute = input("Qual letra ?")

        # utilizamos uma palavra reservada que diz
        # para cada letra na palavra_secreta nos mostre
        for letra in palavra_secreta:
            # se chute == letra da palavra entao print
            if (chute == letra):
                print(letra)

        print("jogando")


    print("Fim de jogo")

# se nome for chamado então executa senão não executa
if(__name__ == "__main__"):
    jogar()
