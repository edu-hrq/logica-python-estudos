''' EXERCICIO 1: RELATÓRIO DE MARGEM DE LUCRO (SETOR FINANCEIRO)
Uma empresa de varejo precisa de um resumo rápido sobre a performance de um produto. Dado o faturamento de R$ 45.000,00 e o custo de R$ 23.500,00,
crie um programa que calcule o lucro e a margem de lucro (lucro dividido pelo faturamento). 
Exiba uma mensagem formatada onde o lucro use o separador de milhar e duas casas decimais, e a margem seja exibida como uma porcentagem inteira.
'''
faturamento = 45000
custo = 23500
lucro = faturamento - custo
margem_lucro = (lucro / faturamento) * 100
print(f'Resposta do Exercício 1: O Lucro nas vendas do Produto foi de R$ {lucro:,.2f}. Isso equivale a {margem_lucro:.0f}%.\n')

''' EXERCÍCIO 2: PADRONIZAÇÃO DE DADOS DE CRM (SETOR DE VENDA)
Um vendedor cadastrouum cliente com os dados desorganizados no sistema: nome = " mArCoS aNtOnIo rOcHa " e email = " MARCOS.ROCHA@GMAIL.COM ". 
Para evitar duplicidade e erros de envio, você deve:
1. Remover os espaços extras no início e fim das duas variáveis.
2. Deixar o nome apenas com as primeiras letras de cada palavra em maiúsculo (formato de nome próprio).
3. Deixar o e-mail todo em letras minúsculas. Exiba os resultados finais no console.
'''
nome = ' mArCoS aNtOnIo rOcHa '
email = ' MARCOS.ROCHA@GMAIL.COM '
nome = nome.strip().title() # strip tira os espaços vazios, title deixa as primeiras letras maiúsculas
email = email.strip().lower() # strip tira os espaços vazios, lower deixa todas as letas minúsculas
print(f'Resposta do Exercíco 2: Nome do colaborador: {nome}. E-mail do colaborador: {email}\n')

''' EXERCICIO 3: MIGRAÇÃO DE SERVIDOR DE E-MAIL (SETOR DE TI)
Sua empresa mudou de nome e todos os funcionários que usavam o domínio @empresa.com.br agora devem usar o domínio @grupocorp.com.
O e-mail do funcionário é andre_silva@empresa.com.br. Crie um código que substitua automaticamente o domínio antigo pelo novo e exiba o novo endereço de e-mail.
'''
email = 'eduardo.silva@empresa.com.br'
novo_dominio = '@grupocorp.com'
email = email.replace('@empresa.com.br', novo_dominio) # substituição do dominio antigo pelo novo
print(f'Resposta do Exercício 3: {email}\n')

''' EXERCÍCIO 4: EXTRAÇÃO DE USERNAME PARA LOG (SETOR DE SEGURANÇA)
Para criar um log de acessos, o sistema precisa extrair apenas a parte do nome do usuário de um e-mail corporativo (tudo o que vem antes do @).
Dado o e-mail beatriz.oliveira@grupocorp.com, use a função .find() e o fatiamento de texto para extrair e exibir apenas o nome beatriz.oliveira.
'''
email = 'beatriz.oliveira@grupocorp.com'
posicao_a = email.find('@') # localização da posição do @ na string
username = email[:posicao_a] # decreta que a variavel username será o email até onde está a posição do @
print(f'Resposta do Exercício 4: {username}\n')

''' EXERCÍCIO 5: PERSONALIZAÇÃO DE EMAIL DE MARKETING (SETOR DE MARKETING)
O marketing quer enviar um e-mail de boas-vindas. O cliente forneceu o nome completo: lucas ferreira souza. 
Você deve extrair apenas o primeiro nome para usar na saudação (ex: "Olá, Lucas!"). O código deve:
1. Encontrar a posição do primeiro espaço.
2. Fatiar o texto para pegar apenas o primeiro nome.
3. Formatar o nome com a primeira letra maiúscula.
4. Exibir a mensagem: "Olá, [Primeiro Nome], seja bem-vindo ao nosso clube!"
'''
mensagem = 'Olá, [Primeiro Nome], seja bem-vindo ao nosso clube!'
nome = 'lucas ferreira souza'
posicao_espaco = nome.find(' ') # localiza o primeiro espaço no texto
pri_nome = nome[:posicao_espaco].capitalize() # variavel pri_nome será nome até onde está o primeiro espaço e deixa a primeira letra maiúscula
mensagem = mensagem.replace('[Primeiro Nome]', pri_nome)
print(f'Resposta do Exercício 5: {mensagem}\n')