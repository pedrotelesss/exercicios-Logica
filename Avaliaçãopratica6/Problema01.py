#Desenvolva uma função que recebe uma mensagem e um número, ela mostra a mensagem e o número e não retorna nada. A função main chama a função passando os dois argumentos lidos, ou seja, digitados pelo usuário.
def recebido (mensagem, numero):
    print(f"A mensagem recebida foi: {mensagem}")
    print(f"O número recebido foi: {numero}")
if __name__ == '__main__':
    mensagem = input("Digite sua mensagem:")
    numero = int(input("Informe um número:"))
    recebido(mensagem, numero)