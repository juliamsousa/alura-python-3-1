import random


def welcome_message():
    print("=================================")
    print("Bem vindo ao jogo de forca!")
    print("=================================")


def load_secret_word(file_name="palavras.txt"):
    # abre o arquivo que contem nossas palavras
    file = open(file_name, "r")
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

    return secret_word


def initialize_correct_letters(secret_word):
    return ["_" for letter in secret_word]


def request_guess():
    return input("Chute uma letra:").strip().upper()


def verify_correct_guess(secret_word, guess, correct_letters):
    index = 0
    for letter in secret_word:
        # trata a diferenciacao de letras maiusculass e minusculas
        if (guess == letter):
            correct_letters[index] = letter
            print("Acertou")
        index += 1

    return correct_letters


def won_game():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def lost_game(secret_word):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {secret_word}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def play():
    welcome_message()
    secret_word = load_secret_word()

    correct_letters = initialize_correct_letters(secret_word)
    print(correct_letters)

    hung = False
    guessed = False
    total_attempts = 0

    while (not hung and not guessed):
        guess = request_guess()

        if (guess in secret_word):
            correct_letters = verify_correct_guess(secret_word, guess, correct_letters)
        else:
            total_attempts += 1
            desenha_forca(total_attempts)
            print(f"Chute errado, faltam {6 - total_attempts} tentativas")

        # verifica se o usuario ultrapassou o n de erros permitidos
        hung = total_attempts == 7
        # verifica se ainda ha letras nao adivinhadas
        guessed = not "_" in correct_letters
        print(correct_letters)

    # apos o loop verifica se o usuario ganhou ou n
    if (guessed):
        won_game()
    else:
        lost_game(secret_word)


if (__name__ == "__main__"):
    play()
