import random


def jogar():
    print('*' * 30)
    print('Bem vindo ao jogo')
    print('*' * 30)

    numero_secreto = random.randrange(1, 11)
    total_de_tentativas = 0
    pontos = 50

    print('Qual nível de dificuldade você quer? ')
    print('(1) Fácil (2) Médio (3) Difícil')

    nivel = int(input('Defina um nível: '))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa", rodada, "de", total_de_tentativas)
        chute_str = input("Digite o seu número de 1 a 10: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)
        if chute < 1 or chute > 10:
            print('Você deve digitar um número entre 1 e 10')
            continue
        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Você acertou! e fez {} pontos".format(pontos))
            break
        else:
            if maior:
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif menor:
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")


if __name__ == '__main__':
    jogar()
