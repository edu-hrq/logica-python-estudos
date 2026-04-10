# EXERCÍCIO 1: CÁLCULO DE BÔNUS DE VENDAS
print('---------- Exercício 1 ----------\n')
faturamento = 50000
bonus = faturamento * 0.10
faturamento_final = faturamento - bonus
print(f'O valor do bônus foi de: R$ {bonus:,.2f}. O valor do faturamento final foi de: R$ {faturamento_final:,.2f}')

# EXERCÍCIO 2: CONTROLE DE ESTOQUE E-COMMERCE   
print('---------- Exercício 2 ----------\n')
estoque = 250
saida_estoque = 78
entrada_estoque = 100
estoque_final = estoque - saida_estoque + entrada_estoque
print(f'Quantidade de celulares no estoque no início do dia: {estoque}. Quantidade de celulares no estoque no final do dia: {estoque_final}')

# EXERCÍCIO 3: DIVISÃO DE CARGAS
print('---------- Exercício 3 ----------\n')
qtd_caixas = 1250
limite_caminhao = 12
caminhoes_cheios = qtd_caixas // limite_caminhao
sobra = qtd_caixas % limite_caminhao
print(f'{caminhoes_cheios} caminhões saíram totalmente cheios. Na viagem menor, irão {sobra} caixas.')

# EXERCÍCIO 4: ANÁLISE DE LUCRO
print('---------- Exercício 4 ----------\n')
fat_consultoria  = 15000
custo_fixo = 5000
imposto_fat = fat_consultoria * 0.15
lucro = fat_consultoria - custo_fixo - imposto_fat
margem_lucro = lucro / fat_consultoria
percent_lucro = margem_lucro * 100
meta_atingida = margem_lucro > 0.30 # verifica e retorna true caso a margem seja maior que 0.30

print(f'Faturamento total: {fat_consultoria} | Custo fixo: {custo_fixo} | Imposto: {imposto_fat} | Lucro: {lucro} | Margem de Lucro: {percent_lucro:.2f}%')
print(meta_atingida)

# EXERCÍCIO 5: CONVERSÃO DE TEMPO DE CONTRATO
print('---------- Exercício 5 ----------\n')
contrato = 40
contrato_anos = contrato // 12
contrato_meses = contrato % 12
print(f'O contrato tem {contrato_anos} anos e {contrato_meses} meses de duração.')