#Construa o programa que tendo como dados de entrada dois pontos quaisquer do plano cartesiano, P(x1, y1) e Q(x2, y2), calcule a distância entre eles
import math
x1 = int(input('Digite a coordenada X do ponto A:'))
y1 = int(input('Digite a coordenada Y do ponto A:'))
x2 = int(input('Digite a coordenada X do ponto B:'))
y2 = int(input('Digite a coordenada Y do ponto B:'))
distancia = ((x2-x1)**2+(y2-y1)**2)
raiz = math.sqrt(distancia)
print(f'A distância entre os pontos A e B é de: {raiz}')