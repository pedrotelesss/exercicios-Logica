#2. Elabore o programa que gere a sequência dos números naturais múltiplos de 3 até 21. Mostre também a soma dos números da sequência gerados, use somador.
soma = 0
for numero in range (0, 21+1,3):
    print(numero, end=" ")
    soma+= numero
print(f"\nA soma dos números é igual a {soma}")