#. Desenvolva o programa que classifique dois valores inteiros quaisquer em ordem crescente. Os valores serão fornecidos pelo usuário.
num1 = int(input('Digite um valor inteiro:'))
num2 = int(input('Digite outro valor inteiro:'))
if num1<num2:
    print(f'{num1, num2}')
else:
    print(f'{num2, num1}')