#Dado o comprimento das três retas a, b e c. Verifique se eles podem ser o comprimento dos lados de um triângulo. Se forem, verifique se compõem um triângulo equilátero, isósceles ou escaleno. Informe se não compuserem nenhum triângulo.
reta1 = float(input('Digite o comprimento da primeira reta:'))
reta2 = float(input('Digite o comprimento da segunda reta:'))
reta3 = float(input('Digite o comprimento da terceira reta:'))
if reta1+reta2<=reta3 or reta1+reta3<=reta2 or reta2+reta3<=reta1:
    print('Não é um triângulo')
elif reta1==reta2==reta3:
    print('O triângulo é equilátero')
elif reta1==reta2 or reta1==reta3 or reta2==reta3:
    print('O triângulo é isósceles')
else:
    print('O triângulo é escaleno')