#Desenvolva o programa que classifique dois valores inteiros quaisquer em ordem crescente. Os valores serão fornecidos pelo usuário.
num1 = int(input('Digite um número:'))
num2 = int(input('Digite outro número:'))
if num1>num2:
    print(f'A ordem crescente dos valores é: {num2,num1}')
else:
    print(f'A ordem crescente dos valores é: {num1,num2}')