'''Exercício 1: Atualização de Cadastro de Clientes (Setor de CRM)
Você tem um dicionário com o faturamento acumulado de alguns clientes: clientes = {"Lira": 5000, "Alon": 3000, "Julia": 4500}. 
O cliente "Alon" fez uma nova compra de R$ 1.500,00. Crie um código que:
1. Atualize o valor do cliente "Alon" somando o novo valor ao faturamento antigo.
2. Adicione um novo cliente chamado "Marcos" com um faturamento inicial de R$ 2.000,00.
3. Exiba o dicionário atualizado.'''

clientes = {
    "Lira": 5000,
    "Alon": 3000,
    "Julia": 4500
    }
nova_compra = 1500
clientes["Alon"] = clientes["Alon"] + nova_compra # soma valor da var nova_compra à chave "Alon"
clientes["Marcos"] = 2000 # parâmetro passado em [] representa uma nova chave, o valor recebido representa o atributo dessa chave
print(f'Resposta do Exercício 1:\n{clientes}\n')


'''Exercício 2: Consulta de Estoque Interativa (Setor de Logística)
A empresa possui o seguinte estoque: estoque = {"teclado": 50, "mouse": 120, "monitor": 30}. Crie um programa que peça para o usuário digitar o nome de um produto.
1. Se o produto existir no estoque, exiba a quantidade disponível.
2. Se o produto não existir, exiba a mensagem: "Produto não encontrado no sistema".
Dica: Lembre-se de tratar o input para evitar erros de letras maiúsculas ou espaços.'''

estoque = {
    "teclado": 50,
    "mouse": 120,
    "monitor": 30
    }
produto = input('Digite o nome do produto: ').strip().lower() # tratamento dos dados

if produto in estoque:
    print(f'Resposta do Exercício 2:\nProduto {produto} encontrado no estoque - Quantidade: {estoque[produto]}\n') # estoque[produto] representa o que foi digitado na var produto e diz o valor da chave
else:
    print(f'Resposta do Exercício 2:\nProduto {produto} não encontrado no sistema\n')


'''Exercício 3: Análise de Faturamento por Região (Setor Financeiro)
Dada a lista de faturamento por região: vendas_regiao = {"Norte": 15000, "Sul": 22000, "Leste": 18000, "Oeste": 25000}. Seu programa deve:
1. Extrair todos os valores (faturamentos) para uma lista.
2. Calcular e exibir o faturamento total da empresa (soma de todas as regiões).
3. Calcular e exibir o faturamento médio das regiões.'''

vendas_regiao = {
    "Norte": 15000,
    "Sul": 22000,
    "Leste": 18000,
    "Oeste": 25000
    }
lista = list(vendas_regiao.values()) # list() é uma função para construir listas no python, values() pega os valores presentes em todo o dicionario citado
soma = sum(lista)
media = soma / len(lista)
print(f'Resposta do Exercício 3:\nLista: {lista} | Soma de todas as regiões: {soma} | Média de todas as regiões: {media}\n')

'''Exercício 4: Sistema de RH – Média de Desempenho (Setor de RH)
O RH armazena as últimas 3 notas de desempenho de cada funcionário em um dicionário: desempenho = {"Lira": [8, 9, 7], "Paula": [10, 9, 10], "Tiago": [6, 7, 8]}.
O gestor quer saber a média da funcionária "Paula". Crie um código que:
1. Acesse a lista de notas da "Paula".
2. Calcule a média das notas (soma das notas dividida pela quantidade de notas).
3. Exiba o resultado: "A média de Paula foi [media]".'''

desempenho = {
    "Lira": [8, 9, 7],
    "Paula": [10, 9, 10],
    "Tiago": [6, 7, 8]
    }
nome = input('Digite o nome do colaborador: ').strip().title() # coleta o nome do colaborador

notas = desempenho[nome] # var criada para pegar a nota do colaborador (se estiver na lista)
media = sum(notas) / len(notas) # var criada para calcular media de notas do colaborador
print(f'Respostas do exercício 4:\nNome: {nome}\nNotas: {notas}\nMédia do colaborador: {media:.2f}\n')

'''Exercício 5: Limpeza de Banco de Dados (Setor de TI)
O sistema de e-commerce descontinuou alguns produtos. Você tem o dicionário: produtos = {"celular": 1500, "camera": 800, "radio": 200, "fone": 100}.
O item "radio" deve ser removido por estar obsoleto. Crie um código que:
1. Remova o item "radio" do dicionário usando o método .pop().
2. Imprima o valor do produto que foi removido para fins de log.
3. Verifique se o produto "celular" ainda existe no dicionário e imprima True ou False.'''

produtos = {
    "celular": 1500,
    "camera": 800,
    "radio": 200,
    "fone": 100
    }
produtos.pop("radio")
print('Respostas do Exercício 5:')
print(produtos)
if "celular" in produtos:
    print(True)
else:
    print(False)