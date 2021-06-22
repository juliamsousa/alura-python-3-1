
def play():
    print ("=================================")
    print ("Bem vindo ao jogo de forca!")
    print ("=================================")

    secret_word = "banana"
    hung = False
    guessed = False
    correct_letters = ["_", "_", "_", "_", "_", "_"]

    print(correct_letters)

    while (not hung and not guessed):
        guess = input("Chute uma letra:" )
        # retira caracteres indesejados da string
        guess = guess.strip()
        print(guess)
        index = 0

        for letter in secret_word:
            # trata a diferenciacao de letras maiusculass e minusculas
            if (guess.upper() == letter.upper()):
                correct_letters[index] = letter
                print("Acertou")
            index = index + 1

        print(correct_letters)

if(__name__=="__main__"):
    play()