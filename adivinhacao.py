print ("=================================")
print ("Bem vindo ao jogo de adivinhacao!")
print ("=================================")

secret_number = 42
total_attempts = 10
round = 1

# for e um laco alternativo ao while e implementa o incremento de forma mais facil
# for <variavel> in range (a, b, step):
# for <variavel> in range [1, 2, 3, ..., n]:
# o conjunto eh (a, b], ou seja o limite superior nao esta incluso

for round in range (1, total_attempts+1):
    # utilizamos a funcao format (f) que aplica a string interpolation
    print(f"Tentativa {round} de {total_attempts}")
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

print ("Fim de jogo!")