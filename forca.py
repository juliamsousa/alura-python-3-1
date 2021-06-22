import random

def play():
    print ("=================================")
    print ("Bem vindo ao jogo de forca!")
    print ("=================================")

    # abre o arquivo que contem nossas palavras
    file = open("palavras.txt", "r")
    # lista que armazenara as palavras do arquivo
    words = []

    # le as linhas do arquivo
    for line in file:
        # retira caracteres indesejados da linha
        line = line.strip()
        words.append(line)

    file.close()

    # sorteia uma palavra randomicamente
    selected_word = random.randrange(0, len(words))

    secret_word = words[selected_word].upper()
    hung = False
    guessed = False
    total_attempts = 0
    correct_letters = ["_" for letter in secret_word]

    print(correct_letters)

    while (not hung and not guessed):
        guess = input("Chute uma letra:" )
        # retira caracteres indesejados da string
        guess = guess.strip().upper()
        print(guess)

        if(guess in secret_word):
            index = 0

            for letter in secret_word:
                # trata a diferenciacao de letras maiusculass e minusculas
                if (guess == letter):
                    correct_letters[index] = letter
                    print("Acertou")
                index += 1

        else:
            total_attempts += 1
            print (f"Chute errado, faltam {6-total_attempts} tentativas")

        # verifica se o usuario ultrapassou o n de erros permitidos
        hung = total_attempts == 6
        # verifica se ainda ha letras nao adivinhadas
        guessed = not "_" in correct_letters
        print(correct_letters)

    #apos o loop verifica se o usuario ganhou ou n
    if(guessed):
        print("Parabéns, você acertou!")
    else:
        print("Você perdeu :c")

if(__name__=="__main__"):
    play()