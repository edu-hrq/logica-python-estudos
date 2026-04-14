'''Exercício 1: Calculadora de Imposto sobre Vendas (Setor Fiscal)
Uma empresa de serviços precisa calcular o imposto de 15% sobre o valor bruto de uma nota fiscal. Como o valor muitas vezes vem copiado de planilhas com "R$" e vírgula, seu programa deve:
1. Pedir para o usuário digitar o valor bruto (Ex: R$ 5.000,00).
2. Limpar o texto removendo o "R$" e trocando a vírgula por ponto.
3. Converter para número decimal (float).
4. Calcular o valor do imposto (15% do valor bruto).
5. Exibir uma mensagem formatada com f-string mostrando o valor do imposto com duas casas decimais.'''

valor = input('Digite o valor bruto: ')
valor = valor.replace('R$', '').replace('.', '').replace(',', '.') # tratamento do que deve ser removido / realocado
valor = float(valor) # troca de tipo para que seja feito cálculo

imposto = valor * 0.15 # cálculo do imposto sobre o valor inserido
print(f'Resposta do Exercício 1:\nValor da NF: {valor:,.2f} | Valor do imposto da NF: {imposto:,.2f}\n')

'''Exercício 2: Sistema de Cadastro de Colaborador (Setor de RH)
Ao cadastrar um novo funcionário, o RH precisa extrair o primeiro nome para criar um crachá e padronizar o e-mail. Crie um programa que:
1. Peça o nome completo do colaborador.
2. Peça o e-mail pessoal do colaborador.
3. Extraia o primeiro nome (deixe-o com a primeira letra maiúscula).
4. Padronize o e-mail (remova espaços extras e deixe tudo em letras minúsculas).
5. Exiba a mensagem: "Cadastro concluído: [Primeiro Nome]. E-mail de acesso: [E-mail padronizado]".'''

nome = str(input('Digite o nome completo do colaborador: '))
email = str(input('Digite o email do colaborador : '))

nome = nome.strip() # tratamento do nome
email = email.strip().lower() # tratamento do email

posicao_espaco = nome.find(' ')
pri_nome = nome[:posicao_espaco].capitalize() # separação do primeiro nome

print(f'Resposta do Exercício 2:\nCadastro concluído: {pri_nome}. E-mail de acesso: {email}\n')

'''Exercício 3: Análise de Metas de Vendas (Setor Comercial)
Um gerente quer comparar o desempenho de duas filiais. O programa deve:
1. Pedir o faturamento da Loja A e o faturamento da Loja B (o usuário pode digitar
números decimais).
2. Calcular o faturamento total das duas lojas.
3. Calcular a média de faturamento entre elas.
4. Exibir uma única mensagem formatada informando o total e a média, utilizando o separador de milhar e duas casas decimais.'''

fat_loja_a = input('Digite o faturamento da Loja A: ')
fat_loja_b = input('Digite o faturamento da Loja B: ')

fat_loja_a = fat_loja_a.replace("R$", "").replace(".", "").replace(",", ".")
fat_loja_a = float(fat_loja_a)
fat_loja_b = fat_loja_b.replace("R$", "").replace(".", "").replace(",", ".")
fat_loja_b = float(fat_loja_b)

total_fat = fat_loja_a + fat_loja_b
media_fat = total_fat / 2

print(f'Resposta do Exercício 3:\nFaturamento total: R$ {total_fat:,.2f} | Média de faturamento: R$ {media_fat:,.2f}\n')