def imc(peso, altura):
    valor_imc = peso / (altura*altura)
    print(valor_imc)
    if valor_imc < 20.7:
        print('Abaixo do peso')
    elif valor_imc >= 20.8 and valor_imc <= 26.4:
        print('Peso normal')
    elif valor_imc >= 26.5 and valor_imc <= 27.8:
        print('Sobrepeso')
    elif valor_imc >= 27.8 and valor_imc <= 31.1:
        print('Obesidade')
    elif valor_imc >= 31.2:
        print('Obesidade mórbida')
