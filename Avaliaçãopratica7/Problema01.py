#Desenvolva a função (def) positivo nulo negativo que recebe um número qualquer real e não retorna nada. Ela mostra a mensagem “Valor Positivo”, se o número recebido for positivo; mostra a mensagem “Valor nulo”, se o número recebido for nulo e mostra a mensagem “Valor negativo”, se o número recebido for negativo. O programa (main) lê o número, chama a função positivo nulo negativo passando o valor lido (argumento).
def analise (x):
    if x > 0:
        print(f"O número {x} é positivo")
    elif x < 0:
        print(f"O número {x} é negativo")
    else:
        print(f"O número {x} é nulo")
if __name__ == '__main__':
    x = int(input("Informe um número:"))
    analise(x)