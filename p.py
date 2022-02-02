cont = 0
valorRef = 0

qtdBens = int(input('Digite a quantidade de bens: '))

while qtdBens < 4:
    qtdBens = int(input('Digite uma quantidade valida de bens:'))

while qtdBens > cont:
    print(f'Bem #{cont+1}')
    valorRef = float(input('Informe o valor de referencia:'))
    qtdOfertas = int(input('Digite a quantidade de ofertas:'))

    while qtdOfertas < 3:
        qtdOfertas = int(input('Digite uma quantidade valida de ofertas:'))

    while qtdOfertas != 0:
        valorOferta = float(input('Informe o valor da oferta:'))
      
        if valorOferta >= valorRef:
            print('Oferta aceita')
            valorRef = valorOferta
        else:
            print('Oferta rejeitada!')
        qtdOfertas = qtdOfertas - 1
    cont = cont + 1

    print(f'Oferta aceita para o bem: {valorRef:.2f}')