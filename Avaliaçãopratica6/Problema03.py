#Crie uma função para somar três valores. Ela recebe os três valores, calcula a soma e retorna o resultado do cálculo. A função main lê os três valores inteiros, chama a função passando os valores lidos e depois mostra o valor retornado pela função, ou seja, o resultado obtido.
def soma_valores (A, B, C):
    soma = A + B + C
    return soma
if __name__ == '__main__':
    A = int(input("Informe o primeiro valor:"))
    B = int(input("Informe o segundo valor:"))
    C = int(input("Informe o terceiro valor:"))
    print(f"A soma de {A} + {B} + {C} é igual a {soma_valores(A, B, C)}")