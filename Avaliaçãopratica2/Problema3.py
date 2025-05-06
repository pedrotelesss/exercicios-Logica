#Refaça o exercício anterior utilizando também operador lógico (e, ou, não).
num1 = int(input('Digite o primeiro número:'))
num2 = int(input('Digite o segundo número:'))
num3 = int(input('Digite o terceiro número:'))
if num1>num2>=num3:
    print(f'O maior valor é o {num1}')
elif num2>num3>=num1:
    print(f'O maior valor é o número {num2}')
else:
    print(f'O maior valor é o número {num3}')