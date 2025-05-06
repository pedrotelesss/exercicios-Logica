#Desenvolva o programa que leia vários valores reais e no final mostre as seguintes informações: A quantidade de valores digitados; A soma dos valores digitados; A média aritmética dos valores digitados; E a quantidade de valores digitados maior que 20.
ct = 0
ct_maior = 0
soma = 0
print('Para sair do loop digite o valor [0]')
while True:
    numero = int(input('Digite qualquer valor:'))
    if numero == 0:
        break
    elif numero >= 20:
        ct_maior += 1
    soma += numero
    ct += 1
print (f'Valores digitados {ct}\nSoma dos valores digitados: {soma}\nMédia aritmética dos valores digitados {soma/ct}\nQuantidade de valores digitados maiores do que 20: {ct_maior}')