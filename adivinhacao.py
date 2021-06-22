import random

print ("=================================")
print ("Bem vindo ao jogo de adivinhacao!")
print ("=================================")

# gerando o numero aleatorio
secret_number = random.randrange(1, 101)
total_attempts = 0
total_points = 1000

print("Selecione um nível de dificuldade")
print(" 1 - Fácil")
print(" 2 - Médio")
print(" 3 - Difícil")

difficulty_level = int(input("Defina a dificuldade:"))

if (difficulty_level == 1):
    total_attempts = 20
elif (difficulty_level == 2):
    total_attempts = 10
else:
    total_attempts = 5

round = 1
inferior_limit = 1
superior_limit = 100

# for e um laco alternativo ao while e implementa o incremento de forma mais facil
# for <variavel> in range (a, b, step):
# for <variavel> in range [1, 2, 3, ..., n]:
# o conjunto eh (a, b], ou seja o limite superior nao esta incluso

for round in range (1, total_attempts+1):
    # utilizamos a funcao format (f) que aplica a string interpolation
    print(f"Tentativa {round} de {total_attempts}")

    # convertemos a input para int, pois em alguns casos vem com tipo <str>
    guess = int(input(f"Digite um número entre {inferior_limit} e {superior_limit}: "))
    print("Voce digitou", guess)

    # convertemos guess para <str> para melhorar a visualizacao do texto
    # com isso podemos concatenar as strings com o operador +
    if (guess < inferior_limit or guess > superior_limit):
        print(f"Você deve digitar um número dentro do intervalo {inferior_limit} : {superior_limit}")
        continue

    # tornando o codigo mais legivel
    guessed = guess == secret_number
    bigger_than = guess > secret_number
    smaller_than = guess < secret_number

    # desse modo temos apenas um chute
    if (guessed):
        print (f"Acertou miseravi! Pontos totais: {total_points}")
        break
    else:
        if (bigger_than):
            print ("Errooooou! Chutou na lua")
        # com o elif caso o teste acima seja verdade, nao e testado
        # nesse caso poderia ser resolvido com um if, mas e pra carater didatico
        elif (smaller_than):
            print ("Errooooou! Pode subir")

        lost_points =  abs(secret_number - guess)
        total_points  = total_points - lost_points

print ("Fim de jogo!")