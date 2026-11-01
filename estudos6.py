print('Escolha o que deseja comprar:')
print('1 - maça')
print('2 - laranja')
print('3 - banana')
produto = int(input('Qual sua escolha? '))
quantidade = int(input('Quantas unidades? '))
if (produto == 1):
    pagar = quantidade * 2.3
    print(f'Você comprou {quantidade} maças. Total à pagar: {pagar}')
else:
    if (produto == 3):
        pagar = quantidade * 1.85
        print(f'Você comprou {quantidade} bananas. Total à pagar: {pagar}')
    else:
        pagar = quantidade * 3.6
        print(f'Você comprou {quantidade} laranjas. Total à pagar: {pagar}')