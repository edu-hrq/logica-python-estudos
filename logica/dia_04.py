'''Exercício 1: Dashboard de Vendas (Análise de Dados)
Você recebeu uma lista com as vendas diárias de uma equipe: vendas = [1500, 2000, 800, 3500, 1200]. Crie um programa que exiba um pequeno relatório contendo:
1. O total de vendas na semana.
2. A média de vendas diária.
3. O valor da melhor venda e da pior venda do período.'''

vendas_diarias = [1500, 2000, 800, 3500, 1200]
soma = sum(vendas_diarias) # variável que armazena a soma de todos os elementos presentes na lista
media = soma / len(vendas_diarias) # len é o termo para pegar o tamanho da lista, ou seja, a quantidade de elementos
maior = max(vendas_diarias) # variável que armazena o valor máximo da lista
menor = min(vendas_diarias) # variável que armazena o valor mínimo da lista
print(f'Resposta do exercício 1:\nTotal de vendas: {soma} | Média diária: {media} | Melhor venda: {maior} | Pior venda: {menor}\n')

'''Exercício 2: Gestão de Estoque (Edição e Verificação)
Uma loja de eletrônicos possui os seguintes produtos: estoque = ["monitor", "teclado", "mouse", "headset"]. O gerente pediu para:
1. Adicionar o item "webcam" ao final da lista.
2. O "teclado" teve seu nome atualizado para "teclado mecanico". Faça essa
alteração na lista.
3. Verificar se "impressora" está no estoque. O programa deve exibir True ou False.
4. Remover o "mouse" da lista, pois saiu de linha.'''

estoque = ["monitor", "teclado", "mouse", "headset"] # lista de items passada
estoque.append("webcam") # adição de webcam no final da lista
estoque[estoque.index("teclado")] = "teclado mecanico" # substitui o indice que se encontra a palavra "teclado" e coloca "teclado mecanico"
print(f'Resposta do exercício 2:')
print('impressora' in estoque) # verificação se está NA variável (usando in)
estoque.remove("mouse") # remoção do item mouse na lista
print(estoque)
print(' ')

'''Exercício 3: Organização de Preços (Ordenação e Slicing)
Uma importadora listou os preços de frete em dólar: fretes = [50, 80, 20, 150, 40]. Para apresentar em uma reunião, você deve:
1. Ordenar a lista do maior para o menor preço.
2. Pegar os 2 fretes mais caros (usando fatiamento/slicing) e armazenar em uma nova
lista chamada top_fretes.
3. Exibir a lista original ordenada e a lista dos top_fretes.'''

fretes = [50, 80, 20, 150, 40]
fretes.sort(reverse= True) # organiza do maior para o menor por conta do reverse= True como parâmetro dentro do .sort()
top_fretes = fretes[:2] # o índice está ATÉ o indice 2
print(f'Resposta do exercício 3:\nLista original: {fretes} | Lista Top_Fretes: {top_fretes}\n')

'''Exercício 4: Sistema de Logística (Busca e Extensão)
A empresa "LogTrack" tem uma rota de entregas: rota = ["Sao Paulo", "Campinas", "Jundiai", "Sorocaba"].
Novas cidades foram adicionadas por uma empresa parceira: novas_cidades = ["Itu", "Valinhos"]. Seu script deve:
1. Unir as duas listas em uma só (usando extend).
2. Identificar em qual posição (índice) está a cidade de "Sorocaba".
3. Exibir a lista completa e a posição encontrada.
4. Exibir uma mensagem final: “Sorocaba é a Xa cidade da rota”'''

rota = ["Sao Paulo", "Campinas", "Jundiai", "Sorocaba"]
novas_cidades = ["Itu", "Valinhos"]
rota.extend(novas_cidades) # .extend() expande a lista juntando o que está dentro do parâmetro, nesse caso, a variável novas_cidades
posicao_sorocaba = rota.index("Sorocaba")
print(f'Resposta do exercício 4:\nLista completa: {rota}| Posição de Sorocaba na lista: {posicao_sorocaba} | Sorocaba é a {posicao_sorocaba + 1}ª cidade na Rota\n')

'''Exercício 5: Atualização de Preços Interativa (Input + Lista)
Você tem uma lista de preços de produtos: precos = [100.0, 250.0, 500.0] e uma com o nome: vinhos = ["Branco", "Tinto","Champagne"]. Crie um programa interativo que:
1. Peça para o usuário digitar qual o nome do produto.
2. Peça para o usuário digitar o novo preço.
3. Atualize o preço na lista e exiba as listas completas com os nomes e os preços'''

precos = [100.0, 250.0, 500.0]
vinhos = ["Branco", "Tinto","Champagne"]
print(f'Resposta do exercício 5:')
pedido1 = input('Qual o nome do produto?').strip().title() # tratamento de variavel e pedido de nome
pedido2 = float(input('Digite o novo preço do produto: ')) # novo preço
indice = vinhos.index(pedido1) # pegando o indice de onde está o que foi digitado pelo user
precos[indice] = pedido2 # ou seja, com o indice coletado, coloca o preço novo digitado usando o mesmo indice, por ex: branco (ind 0) vai substituir 100.0, pois é indice 0 também
print(vinhos)
print(precos)