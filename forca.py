def jogar():
    print('*' * 30)
    print('Bem vindo a Forca')
    print('*' * 30)

    palavra_secreta = 'banana'.upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    tentativas = 0

    # enquanto(true):
    while (not enforcou and not acertou):

        chute = input("Qual a letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index = index + 1
        else:
            tentativas += 1
        enforcou = tentativas == 6
        acertou = "_" not in letras_acertadas
        print("Você errou, ainda há {} tentativas".format(6 - tentativas))
        print(letras_acertadas)

    if (acertou):
        print("Você ganhou!!")

    else:
        print("Você perdeu! ")

    print("Fim do jogo")


if __name__ == '__main__':
    jogar()
