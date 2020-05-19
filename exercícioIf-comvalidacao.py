#variáveis#
nome = input('Digite seu nome: ')

##iniciando validacao nota1
valid_nota = False
while valid_nota == False:
    notaprova1 = input('Digite a nota da primeira prova: ') ##recebe o valor
    try: ##trata exceções 
        notaprova1 = float(notaprova1) ##tenta converter
        if notaprova1 < 0 or notaprova1 > 10: ##testa se está dentro do espero
            print('Nota inválida. O valo deve se 0 e 10.')
        else: ##se tiver OK muda a variável para seguir em frente
            valid_nota = True
    except:
        print('Nota inválida. Use só numeros e separe os decimais com ponto (ex: 9.5).')

valid_nota = False ##RECOMEÇA        

##nota2 validação
while valid_nota == False:
    notaprova2 = input('Digite a nota da segunda prova: ') ##recebe o valor
    try: ##trata exceções 
        notaprova2 = float(notaprova2) ##tenta converter
        if notaprova2 < 0 or notaprova2 > 10: ##testa se está dentro do esperado
            print('Nota inválida. O valo deve se 0 e 10.')
        else: ##se tiver OK muda a variável para seguir em frente
            valid_nota = True
    except:
        print('Nota inválida. Use só numeros e separe os decimais com ponto (ex: 9.5).')


##validação das faltas
valid_falta = False
while valid_falta == False:
    faltas = input('Digite a quantidade de faltas: ')
    try:
        faltas = int(faltas)
        if faltas >20 or faltas < 0:
            print('Quantidade inválida. Insira de 0 a 20')
        else:
            valid_falta = True
    except:
        print('Formato inválido. Insira somente números!')

        
media = (notaprova1 + notaprova2)/2
limitefaltas = 20*70/100
assid = (20-faltas)/20*100

#condição:
if faltas > limitefaltas:
    if media >= 6:
        resultado = 'Reprovado por falta.'
    elif media < 6:
        resultado= 'Reprovado por média e falta.'
        
if faltas <= limitefaltas:
    if media < 6:
        resultado = 'Reprovado por média.'

if faltas <= limitefaltas:
    if media > 6:
        resultado = 'Aprovado.'

else:
    print ('erro')


print(nome,  ',voce foi',resultado, 'Sua média foi:', media, 'e você teve', faltas, 'faltas. Assiduidade de', assid, '%.' )        

print('Nome:', nome)
print('Média:', media)
print('Assiduidade:', assid,'%')
print('Resultado:', resultado)
