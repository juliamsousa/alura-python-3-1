print ("=================================")
print ("Bem vindo ao jogo de adivinhacao!")
print ("=================================")

secret_number = 42
total_attempts = 10

while (total_attempts > 0):
    print("Tentativas restantes", total_attempts)
    # convertemos a input para int, pois em alguns casos vem com tipo <str>
    guess = int(input("Digite o seu numero: "))

    # convertemos guess para <str> para melhorar a visualizacao do texto
    # com isso podemos concatenar as strings com o operador +
    print("Voce digitou", guess)

    # tornando o codigo mais legivel
    guessed = guess == secret_number
    bigger_than = guess > secret_number
    smaller_than = guess < secret_number

    # desse modo temos apenas um chute
    if (guessed):
        print ("Acertou miseravi!")
    else:
        if (bigger_than):
            print ("Errooooou! Chutou na lua")
        # com o elif caso o teste acima seja verdade, nao e testado
        # nesse caso poderia ser resolvido com um if, mas e pra carater didatico
        elif (smaller_than):
            print ("Errooooou! Pode subir")

    total_attempts = total_attempts - 1

print ("Fim de jogo!")