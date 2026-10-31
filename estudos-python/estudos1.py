# ==================================
# EXERCÍCIO 1 - FUNÇÃO PRINT
# ==================================

print("Olá, mundo!")
print('Também pode ser usado aspas simples')
print(2 + 3)
print('Olá,' + ' Mundo!')

# ==================================
# EXERCÍCIO 2 - OPERAÇÕES
# ==================================
print(10 * ( 5 + 7 / 4))
print(2 + 3 * 3)
print(4 ** 2 // 3 )
print((9 ** 2 + 2) * 6 - 1)

# ==================================
# EXERCÍCIO 3 - VARIÁVEIS
# ==================================
universo = 42
print('O sentido da vida para Douglas, é {}'.format(universo))

# ==================================
# EXERCÍCIO 4 - COMPARAÇÃO BOOLEANA
# ==================================

nota1 = 5
resposta = nota1 >= 7
print(resposta)

nota2 = 10
res = nota2 > 7
print(res)

# ==================================
# EXERCÍCIO 5 - CONCATENAÇÃO
# ==================================

exercicio1 = 'A' + '-' * 10 + 'B'
print(exercicio1)
exercicio2 = 'Python ' + '-' * 5 + ' C ' + '-' * 5 + ' Java ' + '-' * 5 + ' PHP'
print(exercicio2)

# ==================================
# EXERCÍCIO 6 - COMPOSIÇÃO
# ==================================

nota = 8.5
disciplina = 'Algoritmos'
ex1 = 'Vc tirou %f na disciplina' % nota
print(ex1)
ex2 = 'Vc tirou %.2f na disciplicina' % nota
print(ex2)
# %s é para string, e %d numeros inteiros #
ex3 = 'Vc tirou {} na disciplina de {}' .format(nota,disciplina)
print(ex3)

comida_fav = 'sushi'
ano_de_nasc = 2004
res = 2026 - 2004
ex4 = f'Minha comida favorita é {comida_fav} e eu tenho {res} anos'
print(ex4)

# ==================================
# EXERCÍCIO 7 - LEN
# ==================================

nome = 'Lívia Ferraz Rocha'
res = len(nome) <= 15
print(res)

