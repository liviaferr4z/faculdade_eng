x = int (input ('Digite um número inteiro: '))
y = int (input ('Digite outro número inteiro: '))
res1 = 'O resultado da soma de {} com {} é {}.' .format (x, y, x + y)
print(res1)
res2 = f'O resultado da soma de {x} com {y} é {x + y}.'
print(res2)

dias = int (input ('Quantos dias? '))
horas = int (input ('Quantas horas? '))
min = int (input ('Quantos minutos? '))
segundos = int (input ('Quantos segundos? '))
total = segundos + (min * 60) + (horas * 60 * 60) + (dias * 24 * 60 * 60)
ex2 = 'O total de segundos é de {}'.format(total)
print(ex2)