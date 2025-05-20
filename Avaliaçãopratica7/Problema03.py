#Simule uma calculadora com as quatro operações aritméticas. Implemente uma função para cada operação aritmética. Ela recebe dois valores e não retorna nada. A função executa o cálculo e mostra o resultado do cálculo. O usuário fornecerá a operação desejada (operador: +, -, x, / ) e os dois valores dentro do programa (função main) que chamará uma das quatro funções. O resultado do cálculo será mostrado dentro de cada função. Use variável local.
def soma (a,b):
    return a + b
def subtracao (a,b):
    return a - b
def multiplicacao (a,b):
    return a * b
def divisao (a, b):
    return a / b
if __name__ == '__main__':
    operador = str(input("Escolha a operação desejada(+, -, *, /):"))
    n1 = float(input("Digite o primeiro número:"))
    n2 = float(input("Digite o segundo número:"))
    if operador == "+":
        print(f"O valor da soma entre {n1} e {n2} é igual a {soma(n1,n2)}")
    elif operador == "-":
        print(f"O valor da subtração entre {n1} e {n2} é igual a {subtracao(n1,n2)}")
    elif operador == "*":
        print(f"O valor da multiplicação entre {n1} e {n2} é igual a {multiplicacao(n1,n2)}")
    elif operador == "/":
        print(f"O valor da divisão entre {n1} e {n2} é igual a {divisao(n1,n2)}")
    else:
        print("Operador inválido")