m1 = float(input('Digite a nota da primeira matéria: '))
m2 = float(input('Digite a nota da segunda matéria: '))
m3 = float(input('Digite a nota da terceira matéria: '))

if m1 >= 7 and m2 >= 7 and m3 >= 7:
    print('O aluno está aprovado!')
else:
    print('O aluno não passou de ano!')

#Exercicio 2#

x = int(input('Digite um valor inteiro: '))
if x >= 1 and x <= 100 or x >= -100 and x <= -1:
    print('Um dos critérios foi atingido')