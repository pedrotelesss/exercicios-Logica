#Elabore a função (def) valor absoluto que recebe um número qualquer e retorna o valor absoluto (módulo) correspondente. O programa lê o número digitado pelo usuário, chama a função valor absoluto passando o número lido e depois gera a tela de saída com o valor retornado pela função valor absoluto. Lembrando que valor absoluto de um número positivo é ele mesmo e o valor absoluto de um número negativo é ele multiplicado por -1. Não use a função abs da linguagem.
def valor_absoluto (x):
    if x < 0:
        return x * -1
    else:
        return x
if __name__ == '__main__':
    numero = int(input("Informe um número:"))
    print(f"O valor absoluto de {numero} é {valor_absoluto(numero)} ")