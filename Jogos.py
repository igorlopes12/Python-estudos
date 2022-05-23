import adivinha
import forca


print('*' * 30)
print('Escolha o seu jogo')
print('*' * 30)

print('(1) Forca (2) Adivinhação')

jogo = int(input('Qual o jogo ?'))

if jogo == 1:
    print('Jogando Forca')
    forca.jogar()
elif jogo == 2:
    print('Jogando adivinhação')
    adivinha.jogar()

