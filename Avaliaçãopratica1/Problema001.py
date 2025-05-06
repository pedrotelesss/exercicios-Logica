#Implemente o programa que calcule o volume de uma esfera de raio R.
import math
raio = float(input('Digite o valor do raio da esfera:'))
volume = (4/3)*(raio**3)*math.pi
print(f'O volume da sua esfera é de: {volume}')