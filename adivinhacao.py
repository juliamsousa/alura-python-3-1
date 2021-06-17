print ("=================================")
print ("Bem vindo ao jogo de adivinhacao!")
print ("=================================")

secret_number = 42

# convertemos a input para int, pois em alguns casos vem com tipo <str>
guess = int(input("Digite o seu numero: "))

print("Voce digitou ", guess)

if (guess == secret_number):
    print ("Acertou miseravi!")
else:
    print ("Errooooou!")