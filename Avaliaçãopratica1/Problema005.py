#Construa o programa que calcule o peso ideal de uma pessoa. Utilize as seguintes fórmulas: - Se homem, o peso ideal é calculado assim: (72,7 x altura) - 58; - Se mulher, o peso ideal é calculado assim: (62,1 x altura) - 44,7. Analise o problema e verifique quais são os dados que o usuário precisa fornecer (digitar).
altura = float(input('Digite o sua altura:'))
genero = input('Digite seu Gênero (Homem/Mulher):')
if genero == 'Homem':
    print(f'Seu peso ideal é de: {(72.7*altura)-58}')
elif genero == 'Mulher':
    print(f'Seu peso ideal é de: {(62.1*altura)-44.7}')
else:
    print('Digite corretamente o seu Gênero')

