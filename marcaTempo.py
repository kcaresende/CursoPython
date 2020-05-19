import time as t
import matplotlib.pyplot as plt

tempos = []
vezes = []
legenda = []
vez = 1
repete = 3

print('Este programa marcará o tempo gasto para digitar a palavra PROGRAMAÇÃO. Você terá que digitá-la'+str (repete)+ ' vezes.')
input('Aperte ENTER para começar.')

while vez <= repete:
    inicio = t.clock()
    input('Digite a palavra: ')
    fim = t.clock()
    tempo = round(fim - inicio,2)
    tempos.append(tempo)
    vezes.append(vez)
    vezstr = str(vez)+'a vez'
    legenda.append(vezstr)
    vez += 1



plt.xticks(vezes, legenda)
plt.plot(vezes, tempos)
plt.show()
