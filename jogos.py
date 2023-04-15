import adivinhacao
import forca

def escolha_jogo() :
    print("Escolha o seu jogo")
    print("Choose your game ")

    print("(1)Forca (2) adivinhação")

    jogo = int(input("Whats is your game?"))

    if(jogo ==1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo==2):
            print("adivinhação")
            adivinhacao.jogar()
if(__name__ == "__main__") :
    escolha_jogo()