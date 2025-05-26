#Desenvolva o programa que leia vários números digitados pelo usuário e use o valor -1 como condição (flag) de saída da estrutura de repetição. Na tela de saída, mostre a quantidade de números digitados.
lista = []
print("Digite o número [-1] para encerrar o loop")
while True:
    Numero = int(input("Digite números para que façam parte da lista:"))
    if Numero == -1:
        break
    lista.append(Numero)
print(f"A lista possui {len(lista)} números em sua estrutura")