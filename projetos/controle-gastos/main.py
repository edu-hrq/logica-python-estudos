# SISTEMA DE CONTROLE DE GASTOS 
controle = []
def obter_nome():
    while True:
        nome = input('Insira o nome do produto a ser listado: ').strip() # nome do produto e strip para retirar espaços inúteis

        if not nome: # se não possui nada na variável, retorna para o começo
            print('\nO nome não pode ser vazio\n')
            continue
    
        return nome.title()

def obter_valor():
    while True:
        valor_input = input('Digite o valor do produto (ex: 150,00): ').strip() # valor do produto e strip para retirar espaços inúteis

        try: # validação para que o tipo da variável fique correto
            valor = float(valor_input.replace('R$', '').replace('.', '').replace(',', '.')) # tratamento dos dados
            
            if valor <= 0: # verifica se o valor é menor ou igual a 0
                print('\nValor do Gasto não pode ser menor ou igual a 0.\n')
                continue
            
            return valor
        
        except ValueError:
            print('\nValor inválido - Tente novamente.\n')

def adicionar_gasto(): # adiciona o gasto à lista de controle de gastos, com duas chaves - nome e valor
    nome = obter_nome()
    valor = obter_valor()

    gasto = { # adição dos dados ao dicionario
        'nome': nome,
        'valor': valor, 
    }
    controle.append(gasto) # adição do dicionário à lista de controle
    print('\nGasto adicionado com sucesso.\n')

def lista_gasto(): # mostra a lista de controle de gastos
    contador = 1
    if not controle:
        print('\nO controle está vazio.\n')
    else:
        for item in controle:
            print(f"{contador}. {item['nome']} - R$ {item['valor']:,.2f}")
            contador += 1

def total_gasto(): # soma de todos os valores presentes na variável controle de gastos.
    soma = 0
    if not controle:
        print('\nNenhum gasto cadastrado.\n')
    else:
        for item in controle:
            soma += item['valor']
    print(f'================================\n   TOTAL - R$ {soma:,.2f}   \n================================')

def limpa_controle(): # limpar lista de controle de gastos
    confirmacao = input('Você tem certeza de que quer excluir o Controle de Gastos? (S para Sim | N para não) ')
    confirmacao = confirmacao.strip().lower()

    if confirmacao == 's':
        controle.clear()
        print('\nControle de Gastos limpo com sucesso!\n')
    else:
        print('\nLista de Controle de Gastos não foi excluída.')

opcoes = { # dicionário das funções construídas
    1: adicionar_gasto,
    2: lista_gasto,
    3: total_gasto,
    4: limpa_controle,
}

while True: # menu interativo e execução do código
    print('======== CONTROLE DE GASTOS ========\n1 - Adicionar gasto\n2 - Ver lista de gastos\n3 - Ver total dos gastos\n4 - Limpar Controle de Gastos\n0 - Sair\n====================================')
    
    try: # validação da opção selecionada
        opcao = int(input('Digite a opção desejada: '))
    except ValueError: # caso insira um valor inválido com o tipo definido
        print('\nDigite apenas números!\n')
        continue

    if opcao == 0: # sair do programa
        print('Encerrando o programa...')
        break
    if opcao not in opcoes: # caso coloque um valor válido, mas esse valor não esteja presente no dict opcoes
        print('Opção não encontrada, selecione alguma opção presente no menu.')
        continue

    opcoes[opcao]() # chama a função da opção escolhida e executa