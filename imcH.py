def imcH(peso, altura):
    valor_imc = peso / (altura*altura)
    if valor_imc < 20.7:
        print(valor_imc)
        print('Abaixo do peso')
    elif valor_imc >= 20.8 and valor_imc <= 26.4:
        print(valor_imc)
        print('Peso normal')
    elif valor_imc >= 26.5 and valor_imc <= 27.8:
        print(valor_imc)
        print('Sobrepeso')
    elif valor_imc >= 27.8 and valor_imc <= 31.1:
        print(valor_imc)
        print('Obesidade')
    elif valor_imc >= 31.2:
        print(valor_imc)
        print('Obesidade mórbida')
