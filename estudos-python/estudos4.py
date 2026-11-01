data_nasc = int(input("Qual o seu ano de nascimento? "))
ano_atual = int(input("Em que ano estamos? "))
idade = ano_atual - data_nasc
print(f"Você tem {idade} anos de idade")
if (idade >= 18) :
   print("Você é maior de idade")

#EXERCICIO 2#
salario_funcionario = float(input('Informe seu salário: '))
tempo_de_empresa = float(input('Ano de admissão: '))
ano_atual = int(input('Ano atual: '))
tempo = ano_atual - tempo_de_empresa

if (tempo > 5) :
   bonus = salario_funcionario * 0.2
else:
   bonus = salario_funcionario * 0.1
print(f'Você tem {tempo} anos dentro desta empresa')
print(f'Seu salário é de {salario_funcionario}')
print(f'E sua bonificação é de {bonus}')
print(f'Salário final {bonus + salario_funcionario}')
