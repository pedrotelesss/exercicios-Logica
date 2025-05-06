#3. Elabore o programa que gere a sequência do dobro dos números naturais até dez na ordem crescente. Mostre também a soma e a média aritmética da sequência gerada
ct = 0
soma = 0
for numero in range (0,10+1):
    print(numero*2, end=" ")
    ct+=1
    soma+=(numero*2)
media=soma/ct
print(f"\nA quantidade de números mostrados foi de {ct} e a soma deles é igual a {soma}")