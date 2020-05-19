import imc
import imcH

nome = input('Insira seu nome: ')

valida_peso = False

while valida_peso == False:
    peso = input('Insira seu peso, usando ponto para separar os gramas: ')
    try:
        peso = float(peso)
        if peso < 0:
            print('O peso deve ser a partir de 0!')
        else:
            valida_peso = True
    except:
        print('Insira somente numeros usando ponto para separa os gramas')
        

valida_altura = False

while valida_altura == False:
    altura = input('Insira sua altura, usando ponto para separar os centímetros: ')
    try:
        altura = float(altura)
        if altura < 0:
            print('A altura deve ser a partir de 0!')
        else:
            valida_altura = True
    except:
        print('Insira somente numeros usando ponto para separar os centímetros.')

valida_sexo = False
while valida_sexo == False:
    sexo = str(input('Insira seu sexo F ou M: ')).upper()
    if sexo != 'F' and sexo != 'M':
            print('Sexo inexistente na base. Tente novamente: ')
    
    else:
         valida_sexo = True
         print('\n')

print('O seu IMC e classificação são:')

if sexo == 'F':
    imc.imc(peso, altura)
else:
    imcH.imcH(peso, altura)
