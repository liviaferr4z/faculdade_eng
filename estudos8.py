print('Calculadora')
print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Digite outra tecla para sair.')

operacao = input('Qual operação deseja realizar?')
x = int(input('Digite o primeiro valor: '))
y = int(input('Digite o segundo valor: '))

if (operacao == '+'):
    res = x + y
    print(f'Resultado: {x} + {y} = {res}')
elif (operacao == '-'):
    res = x - y
    print(f'Resultado: {x} - {y} = {res}')
elif (operacao == '*'):
    res = x * y
    print(f'Resultado: {x} * {y} = {res}')
elif (operacao == '/'):
    res = x / y
    print(f'Resultado: {x} / {y} = {res}')
else:
    print('Operação inválida')