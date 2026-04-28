'''Exercício 1: Automação de Convites (Setor de Eventos/RH)
A empresa terá um treinamento e você precisa simular o envio de 10 lembretes no console fazendo a contagem
regressiva para aparecer no sistema da empresa. Use a função range() para imprimir 10 vezes a mensagem:
"Lembrete: O treinamento de Python começa em X minutos.'''
contador = 10 # contador dos minutos 
print('Resposta do Exercício 1: ')
for i in range(10):
    print(f'O treinamento de Python começa em {contador} minutos.')
    contador -= 1 # retira 1 a cada vez que o loop se repete
print() # feito para separar adequadamente no terminal

'''Exercício 2: Cálculo de Comissão Progressiva (Setor de Vendas)
Você tem uma lista de vendas de um vendedor: vendas = [2000, 5000, 1000, 8000, 3000]. A regra de comissão é:
● Vendas acima de R$ 4.000,00: comissão de 10%.
● Vendas até R$ 4.000,00: comissão de 5%. Crie um programa que percorra a lista e,
ao final, exiba o valor total que o vendedor receberá de comissão.'''

comissao = 0
vendas = [2000, 5000, 1000, 8000, 3000]
print('Resposta do Exercício 2: ')
for i in vendas:
    if i > 4000:
        comissao = i * 0.1 # se for maior que 4000, a comissão é de 10% do valor
        print(f'Comissão: {comissao}')
    else:
        comissao = i * 0.05 # se for menor, a comissão é de 5% do valor.
        print(f'Comissão: {comissao}')
print()

'''Exercício 3: Verificação de Estoque Crítico (Setor de Logística)
Dada a lista de produtos estoque_produtos = ["monitor", "teclado", "mouse", "headset", "gabinete"] e a lista correspondente de quantidades estoque_quantidades = [5,
12, 2, 8, 15]. O estoque mínimo para qualquer item é 8 unidades.
Crie um programa que percorra as listas e, para cada item que esteja abaixo do mínimo, imprima: "ALERTA: O produto [nome] está com apenas [quantidade] unidades no estoque!".'''

estoque_produtos = ["monitor", "teclado", "mouse", "headset", "gabinete"]
estoque_quantidades = [5, 12, 2, 8, 15]

print('Resposta do Exercício 3: ')

for i in range(len(estoque_produtos)):  # percorre os índices da lista estoque_produtos
    if estoque_quantidades[i] < 8:  # verifica se a quantidade é menor que o mínimo (8)
        print(f'ALERTA: O produto {estoque_produtos[i]} está com apenas {estoque_quantidades[i]} unidades no estoque!')
print()

'''Exercício 4: Análise de Custos Mensais (Setor Financeiro)
Você tem dois dicionários: um com a meta de gastos de cada mês e outro com os gastos reais. metas = {"jan": 1000, "fev": 1200, "mar": 1100} gastos = {"jan": 900, "fev": 1350,
"mar": 1100} Crie um loop que percorra os meses e informe para cada mês:
● Se o gasto foi menor ou igual à meta: "Mês [mês]: Dentro do orçamento."
● Se o gasto ultrapassou a meta: "Mês [mês]: Orçamento estourado em R$[valor da diferença]."'''

metas = {"jan": 1000, "fev": 1200, "mar": 1100}
gastos = {"jan": 900, "fev": 1350, "mar": 1100}

for i in range(len(metas)):
    print(metas[i])
    if gastos[i] <= metas[i]:
        print(f"Mês {metas[i]}: Dentro do orçamento.")
    else:
        print(f"Mês {metas[i]}: Orçamento estourado em.")

'''Exercício 5: Reajuste Geral de Preços (Setor Comercial)
Devido à inflação, a empresa decidiu aumentar o preço de todos os seus produtos em um percentual decidido pelo usuário.
O catálogo atual é: precos = {"celular": 1500, "tablet": 2500, "notebook": 5000}.
1. Peça ao usuário para digitar o percentual de aumento (ex: 10 para 10%).
2. Use um loop para atualizar cada preço dentro do dicionário.
3. Ao final, exiba o novo catálogo de preços formatado.'''