import os
import csv
os.system('clear') or None

from numpy import genfromtxt
import numpy as numpy

pesos = genfromtxt('pesosnovos.csv', delimiter=',')
entrada = genfromtxt('entradanova.csv', delimiter=',')



########### para a primeira linha da matriz de entrada

#distancia euclidiana entre o primeiro neurônio e os imputs
dist11 = (entrada[0] - pesos[0,0])**2 
dist12 = (entrada[1] - pesos[1,0])**2 
dist13 = (entrada[2] - pesos[2,0])**2 
dist14 = (entrada[3] - pesos[3,0])**2 

euclidiana1 = (dist11+dist12+dist13+dist14)

#distancia euclidiana entre o segundo neurônio e os imputs
dist21 = (entrada[0] - pesos[0,1])**2
dist22 = (entrada[1] - pesos[1,1])**2
dist23 = (entrada[2] - pesos[2,1])**2
dist24 = (entrada[3] - pesos[3,1])**2

euclidiana2 = (dist21+dist22+dist23+dist24)

print(euclidiana1)
print(euclidiana2)

if euclidiana1 < euclidiana2:
	print('\n o elemento pertence ao cluster 1')

else:
	print('\n o elemento pertence ao cluster 2')
print('\n')
print(pesos)
print('\n')