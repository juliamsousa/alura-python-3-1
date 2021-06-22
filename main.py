import forca
import adivinhacao

print ("=================================")
print ("Bem vindo ao nosso fliperama!")
print ("=================================")

print("Selecione qual jogo deseja jogar")
print(" 1 - Forca")
print(" 2 - Adivinhação")

game = int(input("Digite o jogo desejado:"))

if(game == 1):
    print("Iniciando o jogo da Forca")
    forca.play()
elif(game == 2):
    print ("Iniciando o jogo da Adivinhação")
    adivinhacao.play()