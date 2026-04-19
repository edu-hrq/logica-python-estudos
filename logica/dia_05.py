'''Exercício 1: Validação de Investimento (Setor Financeiro)
Uma corretora de valores quer automatizar a recomendação básica de perfil. Crie um programa que peça ao usuário o valor que ele deseja investir.
1. Se o valor for menor que R$ 1.000,00, exiba: "Perfil iniciante: Sugerimos Tesouro Direto".
2. Se o valor for entre R$ 1.000,00 e R$ 5.000,00 (inclusive), exiba: "Perfil moderado: Sugerimos Fundos Imobiliários".
3. Se o valor for acima de R$ 5.000,00, exiba: "Perfil arrojado: Sugerimos Ações".
*Lembre-se de tratar o input caso o usuário digite "R$" ou use vírgula.*'''



'''Exercício 2: Controle de Acesso ao Sistema (Setor de Segurança)
Você tem uma lista de e-mails de administradores: admins = ["ana@empresa.com", "guilherme@empresa.com", "felipe@empresa.com"].
Crie um programa que peça o e-mail do usuário. O programa deve:
1. Padronizar o e-mail (letras minúsculas e sem espaços).
2. Verificar se o e-mail está na lista de admins.
3. Se estiver, exibir: "Acesso liberado! Bem-vindo ao painel de controle".
4. Caso contrário, exibir: "Acesso negado. Você não tem permissões de administrador".'''

admins = ["ana@empresa.com", "guilherme@empresa.com", "felipe@empresa.com"]
email = input('Digite seu e-mail: ').strip().lower()
print('Resposta do Exercício 1: ')
if email in admins:
    print('Acesso liberado! Bem-vindo ao painel de controle\n')
else:
    print('Acesso negado. Você não tem permissões de administrador.\n')

'''Exercício 3: Cálculo de Desconto Progressivo (Setor de Vendas)
Um e-commerce aplica descontos automáticos no carrinho. Crie um programa que receba o valor total da compra e aplique a seguinte lógica:
● Compras a partir de R$ 500,00: 15% de desconto.
● Compras a partir de R$ 200,00 (e menos de 500): 10% de desconto.
● Compras abaixo de R$ 200,00: Sem desconto. O programa deve exibir o valor do desconto e o valor final a pagar, formatados em R$.'''

compra = float(input('Digite o valor total da compra: '))
desconto = 0
print('Resposta do Exercício 2: ')
if compra >= 500:
    desconto = compra * 0.15
    total = compra - desconto
    print(f'O valor do desconto é de: R$ {desconto:,.2f} e o valor final a pagar é: R$ {total:,.2f}')
elif compra >= 200:
    desconto = compra * 0.10
    total = compra - desconto
    print(f'O valor do desconto é de: R$ {desconto:,.2f} e o valor final a pagar é: R$ {total:,.2f}')
else:
    desconto = 0
    total = compra - desconto
    print(f'O valor do desconto é de: R$ {desconto:,.2f} e o valor final a pagar é: R$ {total:,.2f}')

'''Exercício 4: Análise de Metas Combinadas (Setor Comercial)
Uma empresa paga bônus se a meta individual do vendedor E a meta da loja forem batidas.
1. Peça as vendas do vendedor e a meta individual dele.
2. Peça as vendas totais da loja e a meta da loja.
3. Se o vendedor bater a meta dele E a loja bater a meta total, o bônus é de 20% sobre as vendas do vendedor.
4. Caso contrário, o bônus é zero. Exiba a mensagem: "Seu bônus este mês é de: R$[valor]".'''

meta_individual = float(input('Qual sua meta individual? '))
vendas_vendedor = float(input('Qual o valor das vendas que você fez? '))

meta_loja = float(input('Qual a meta da loja? '))
vendas_loja = float(input('Qual o total de vendas da loja? '))

if vendas_vendedor >= meta_individual and vendas_loja >= meta_loja:
    bonus = 0.2 * vendas_vendedor
    print(f'')
else:
    bonus = 0

print(f'Resposta do Exercício 4\nSeu bônus este mês é de> R$ {bonus:,.2f}')


'''Exercício 5: Sistema de Triagem de E-mails (Setor de Customer Experience)
Crie um sistema que ajude a filtrar para qual departamento uma reclamação deve ir. O usuário deve digitar o assunto do e-mail.
● Se no assunto aparecer a palavra "pagamento" ou "boleto", exiba: "Encaminhado para o Financeiro".
● Se no assunto aparecer a palavra "entrega" ou "atraso", exiba: "Encaminhado para a Logística".
● Caso não seja nenhum desses, exiba: "Encaminhado para o Suporte Geral". Dica: Use o operador in para verificar se a palavra está dentro do texto.'''


