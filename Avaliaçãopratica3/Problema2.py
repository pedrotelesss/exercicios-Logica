#Implemente o programa que leia a nota de vários alunos de uma turma e gere uma tela de saída com as seguintes informações: a quantidade de alunos aprovados, a quantidade de alunos reprovados e a quantidade de alunos que fizeram a prova. Considere que o aluno será aprovado com nota for maior ou igual a cinco.
ct_reprovados = 0
ct_aprovados = 0
ct_total = 0
print('Para sair do loop digite o valor [-1]')
while True:
    nota = float(input('Digite as notas dos alunos:'))
    if nota == -1:
        break
    elif nota>=5:
        ct_aprovados += 1
    elif nota<5:
        ct_reprovados += 1
    ct_total +=1
print(f'Quantidade de alunos que realizaram a prova: {ct_total}\nAprovados: {ct_aprovados}\nReprovados: {ct_reprovados}')