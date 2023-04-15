import random


def jogar() :
    print("Jogo de Adivinhação")

    tentativas = 0
    numero_secreto = random.randrange(1,10)
    pontos = 100
    print("Qual é o seu nivel ? ")
    print("nivel 1(easy) nivel 2 (medium) niveil 3 (hard)")

    nivel = int(input("defina seu nivel"))

    if(nivel ==1):
        tentativas = 10
    elif(nivel==2):
        tentativas=5
    else:
        tentativas = 3


    for rodada in range(1, tentativas +1):
        print("tentativa {} de {}".format(rodada, tentativas))
        chute_str = input("Digite seu número de 1 até 10:")
        print("você digitou", chute_str)
        chute = int(chute_str)

        if(chute <1 or chute >10):
            print("Deixar de ser monstro e lê direito")
            continue

        acertou = chute ==numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou) :
            print("Parabéns você acertou e fez {} pontos!".format(pontos))
            break
        else :
            if(maior) :
                print("Você errou! O  seu chute foi maior do que número secreto e você temdss {} pontos".format(pontos))

            elif(menor) :
                print("Você errou! O  seu chute foi menor do que número secreto e você tem {} pontos".format(pontos))

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

            print("Finish")

if(__name__ == "__main__") :
    jogar()