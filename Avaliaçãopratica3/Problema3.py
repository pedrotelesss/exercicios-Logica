#Construa o programa que calcule a média aritmética dos números pares e a média aritmética dos números ímpares. O usuário fornecerá os valores de entrada que pode ser um número qualquer par ou ímpar. A condição de saída será o número 0 (zero).
ct_pares = 0
soma_pares = 0
ct_impares = 0
soma_impares = 0
print('Para sair do loop digite o valor [0]')
while True:
    numero = int(input('Digite os números:'))
    if numero==0:
        break
    elif numero%2 == 0:
        ct_pares += 1
        soma_pares += numero
        media_pares = soma_pares/ct_pares
    elif numero%2>0:
        ct_impares +=1
        soma_impares += numero
        media_impares = soma_impares/ct_impares
print(f'A média aritmética dos números pares: {media_pares}\nA média aritmética dos números impares: {media_impares} ')