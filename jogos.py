import forca
import adivinhacao

def escolhe_jogo():
    print("***********************************")
    print("********Escolha o seu jogo!********")
    print("***********************************")

    print("(1) Jogo da Forca (2) Jogo de Adivinhação")
    jogo = int(input("Qual jogo ?"))

    if (jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()
        
# se nome for chamado então executa senão não executa
if(__name__ == "__main__"):
    escolhe_jogo()