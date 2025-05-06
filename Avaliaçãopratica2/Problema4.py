#Elabore o programa que simule a calculadora com as quatro operações aritméticas básicas.
print ('<-------------Calculadora------------>')
num1 = float(input('Digite o primeiro número:'))
num2 = float(input('Digite o segundo número:'))
operacao = input('Escolha a operação desejada (+ , - , * , /):')
if operacao=='+':
    print(f'valor: {num1+num2}')
elif operacao=='-':
    print(f'Valor: {num1-num2}')
elif operacao=='*':
    print(f'Valor: {num1*num2}')
elif operacao=='/':
    print(f'Valor:{num1/num2}')
else:
    print('Use os símbolos que estão entre parênteses')