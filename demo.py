import os
import csv
os.system('clear') or None
from numpy import genfromtxt
import numpy as numpy


pesos = genfromtxt('pesos.csv', delimiter=',')
entrada = genfromtxt('entradatreinamento.csv', delimiter=',')

lr=0.6; #learning rate inicial
tr=0;	#raio topológico
itera=1000; #número de iterações
ativa=1;

#Esse algorítimo considerada o tamanho da vizinhança topológica igual a zero


for x in range(1,itera):
		
	########### Para a primeira linha da matriz de entrada

	#distancia euclidiana entre o primeiro neurônio e os imputs
	dist11 = (entrada[0,0] - pesos[0,0])**2 
	dist12 = (entrada[0,1] - pesos[1,0])**2 
	dist13 = (entrada[0,2] - pesos[2,0])**2 
	dist14 = (entrada[0,3] - pesos[3,0])**2 

	euclidiana1 = (dist11+dist12+dist13+dist14)

	#distancia euclidiana entre o segundo neurônio e os imputs
	dist21 = (entrada[0,0] - pesos[0,1])**2
	dist22 = (entrada[0,1] - pesos[1,1])**2
	dist23 = (entrada[0,2] - pesos[2,1])**2
	dist24 = (entrada[0,3] - pesos[3,1])**2

	euclidiana2 = (dist21+dist22+dist23+dist24)

	print(euclidiana1)
	print(euclidiana2)

	if euclidiana1 < euclidiana2:
		print('o neurônio 1 é o vencedor')
		pesos[0,0]=pesos[0,0]+lr*(entrada[0,0] - pesos[0,0])
		pesos[1,0]=pesos[1,0]+lr*(entrada[0,1] - pesos[1,0])
		pesos[2,0]=pesos[2,0]+lr*(entrada[0,2] - pesos[2,0])
		pesos[3,0]=pesos[3,0]+lr*(entrada[0,3] - pesos[3,0])
	else:
		print('o neurônio 2 é o vencedor')
		pesos[0,1]=pesos[0,1]+lr*(entrada[0,0] - pesos[0,1])
		pesos[1,1]=pesos[1,1]+lr*(entrada[0,1] - pesos[1,1])
		pesos[2,1]=pesos[2,1]+lr*(entrada[0,2] - pesos[2,1])
		pesos[3,1]=pesos[3,1]+lr*(entrada[0,3] - pesos[3,1])

	print(pesos)


	########### para segunda linha da matriz de entrada
	dist11 = (entrada[1,0] - pesos[0,0])**2
	dist12 = (entrada[1,1] - pesos[1,0])**2  
	dist13 = (entrada[1,2] - pesos[2,0])**2  
	dist14 = (entrada[1,3] - pesos[3,0])**2  

	euclidiana1 = (dist11+dist12+dist13+dist14)

	dist21 = (entrada[1,0] - pesos[0,1])**2 
	dist22 = (entrada[1,1] - pesos[1,1])**2 
	dist23 = (entrada[1,2] - pesos[2,1])**2 
	dist24 = (entrada[1,3] - pesos[3,1])**2 

	euclidiana2 = (dist21+dist22+dist23+dist24) 

	print(euclidiana1)
	print(euclidiana2)

	if euclidiana1 < euclidiana2:
		print('o neurônio 1 é o vencedor')
		pesos[0,0]=pesos[0,0]+lr*(entrada[1,0] - pesos[0,0])
		pesos[1,0]=pesos[1,0]+lr*(entrada[1,1] - pesos[1,0])
		pesos[2,0]=pesos[2,0]+lr*(entrada[1,2] - pesos[2,0])
		pesos[3,0]=pesos[3,0]+lr*(entrada[1,3] - pesos[3,0])
	else:
		print('o neurônio 2 é o vencedor')
		pesos[0,1]=pesos[0,1]+lr*(entrada[1,0] - pesos[0,1])
		pesos[1,1]=pesos[1,1]+lr*(entrada[1,1] - pesos[1,1])
		pesos[2,1]=pesos[2,1]+lr*(entrada[1,2] - pesos[2,1])
		pesos[3,1]=pesos[3,1]+lr*(entrada[1,3] - pesos[3,1])

	print(pesos)


	########### para a terceira linha da matriz

	dist11 = (entrada[2,0] - pesos[0,0])**2 
	dist12 = (entrada[2,1] - pesos[1,0])**2 
	dist13 = (entrada[2,2] - pesos[2,0])**2 
	dist14 = (entrada[2,3] - pesos[3,0])**2 

	euclidiana1 = (dist11+dist12+dist13+dist14) 


	dist21 = (entrada[2,0] - pesos[0,1])**2 
	dist22 = (entrada[2,1] - pesos[1,1])**2 
	dist23 = (entrada[2,2] - pesos[2,1])**2 
	dist24 = (entrada[2,3] - pesos[3,1])**2 

	euclidiana2 = (dist21+dist22+dist23+dist24)

	print(euclidiana1)
	print(euclidiana2)

	if euclidiana1<euclidiana2:
		print('o neurônio 1 é o vencedor')
		pesos[0,0]=pesos[0,0]+lr*(entrada[2,0] - pesos[0,0])
		pesos[1,0]=pesos[1,0]+lr*(entrada[2,1] - pesos[1,0])
		pesos[2,0]=pesos[2,0]+lr*(entrada[2,2] - pesos[2,0])
		pesos[3,0]=pesos[3,0]+lr*(entrada[2,3] - pesos[3,0])
	else:
		print('o neurônio 2 é o vencedor')
		pesos[0,1]=pesos[0,1]+lr*(entrada[2,0] - pesos[0,1])
		pesos[1,1]=pesos[1,1]+lr*(entrada[2,1] - pesos[1,1])
		pesos[2,1]=pesos[2,1]+lr*(entrada[2,2] - pesos[2,1])
		pesos[3,1]=pesos[3,1]+lr*(entrada[2,3] - pesos[3,1])

	print(pesos)

	########### para a quarta linha da matriz de entrada

	dist11 = (entrada[3,0] - pesos[0,0])**2 
	dist12 = (entrada[3,1] - pesos[1,0])**2 
	dist13 = (entrada[3,2] - pesos[2,0])**2 
	dist14 = (entrada[3,3] - pesos[3,0])**2 

	euclidiana1 = (dist11+dist12+dist13+dist14)

	dist21 = (entrada[3,0] - pesos[0,1])**2 
	dist22 = (entrada[3,1] - pesos[1,1])**2 
	dist23 = (entrada[3,2] - pesos[2,1])**2 
	dist24 = (entrada[3,3] - pesos[3,1])**2 

	euclidiana2 = (dist21+dist22+dist23+dist24)

	print(euclidiana1)
	print(euclidiana2)

	if euclidiana1<euclidiana2:
		print('o neurônio 1 é o vencedor')
		pesos[0,0]=pesos[0,0]+lr*(entrada[3,0] - pesos[0,0])
		pesos[1,0]=pesos[1,0]+lr*(entrada[3,1] - pesos[1,0])
		pesos[2,0]=pesos[2,0]+lr*(entrada[3,2] - pesos[2,0])
		pesos[3,0]=pesos[3,0]+lr*(entrada[3,3] - pesos[3,0])
	else:
		print('o neurônio 2 é o vencedor')
		pesos[0,1]=pesos[0,1]+lr*(entrada[3,0] - pesos[0,1])
		pesos[1,1]=pesos[1,1]+lr*(entrada[3,1] - pesos[1,1])
		pesos[2,1]=pesos[2,1]+lr*(entrada[3,2] - pesos[2,1])
		pesos[3,1]=pesos[3,1]+lr*(entrada[3,3] - pesos[3,1])

	print(pesos)
	lr=lr/1.05 #usado para diminuir o fator de aprendizado
	
	if x == itera-1:
		os.system('clear') or None
		print('O valor dos pesos converge para:\n')
		print(numpy.round(pesos,1))


#salvo em um novo txt a matrix de pesos
print('\n Os pesos ajustados foram salvos no arquivo pesosnovos.csv \n')
a = numpy.round(pesos,1)
numpy.savetxt("pesosnovos.csv", a, delimiter=",")


