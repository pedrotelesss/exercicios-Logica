#Implemente uma função que calcula a idade de uma pessoa. Ela recebe o ano de nascimento da pessoa, faz o cálculo e retorna à idade. A função principal (main) lê o ano de nascimento digitado pelo usuário, chama a função e mostra o valor retornado pela função calcula.
def calculo_idade (ano_atual, nasc):
    idade = ano_atual - nasc
    return idade
if __name__ == '__main__':
    ano_atual = int(input("Digite o ano atual:"))
    nasc = int(input("Digite o seu ano de nascimento:"))
    print(f"Você nasceu no ano de {nasc} e possui {calculo_idade(ano_atual, nasc)}")