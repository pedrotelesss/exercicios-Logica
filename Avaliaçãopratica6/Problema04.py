#Elabore o problema (o enunciado) de um problema que usa função e resolva o problema proposto, ou seja, faça a implementação da função def e da função principal (main).
#Ver a classificação do triângulo
def classificacao (A, B, C):
    if A > B + C or B > A + C or C > A + B:
        print("As Médidas não são de um triângulo")
    elif A == B == C:
        print("É um triângulo equilátero")
    elif A == B or A == C or B == C:
        print("É um triângulo isósceles")
    elif A != B or A != C or B != C:
        print("É um triângulo escaleno")
if __name__ == '__main__':
    A = int(input("Informe o primeiro lado do triângulo:"))
    B = int(input("Informe o segundo lado do triângulo:"))
    C = int(input("Informe o terceiro lado do triângulo:"))
    (classificacao(A,B,C))