import json # biblioteca json
import os

tarefas = []
caminho = 'dados/tarefas.json'

def salvar_tarefas():
    os.makedirs('dados', exist_ok=True)
    with open(caminho, 'w') as arquivo: # abre (ou cria) arquivo
        json.dump(tarefas, arquivo) # load salva a lista 'tarefas' dentro do arquivo

def carregar_tarefas(): # carregamento de dados já salvos anteriormente
    global tarefas # uso de variável fora da função
    try: # tenta abrir o arquivo
        with open(caminho, 'r') as arquivo: # abre (ou cria) arquivo 'tarefas.json'
            tarefas = json.load(arquivo) # carrega o arquivo 'tarefas.json'
    except FileNotFoundError: # se o arquivo não existir, inicia com uma lista vazia
        tarefas = []

def adicionar_tarefas(): # adição de tarefas à lista 'tarefas'
    tarefa = input('Digite a tarefa: ').strip().title()
    tarefas.append(tarefa)
    salvar_tarefas()
    print(f'Tarefa "{tarefa}" adicionada com sucesso!')

def listar_tarefas(): # listar cada tarefa adicionada
    if not tarefas: # se variavel 'tarefas' estiver vazia
        print('Nenhuma tarefa cadastrada.')
    else:
        for i, tarefa in enumerate(tarefas, start= 1): # contador enumerado no loop para listar tarefa
            print(f'{i}. {tarefa}')

def excluir_lista():
    resposta = input('Tem certeza de que deseja excluir a Lista de Afazeres? (S para Sim | N para Não)').strip().lower()
    if resposta and resposta[0] == 's': # se a resposta inicia com 's':
        tarefas.clear() # limpa a lista de tarefas
        salvar_tarefas() # salva a lista de tarefas excluindo o que estiver no arquivo .json
        print('Lista de Afazeres limpa com sucesso.')
    else:
        print('Lista de Afazeres não foi excluída.')

opcoes = { # dict de opções para o menu
    1: adicionar_tarefas,
    2: listar_tarefas,
    3: excluir_lista,
}

def menu(): # menu do projeto
    while True:
        print(f'======== LISTA DE TAREFAS ========\n'
              '1 - ADICIONAR TAREFAS\n'
              '2 - LISTAR TAREFAS\n'
              '3 - EXCLUIR TODAS AS TAREFAS\n'
              '0 - SAIR\n'
              '==================================='
              )
        
        try: # validação das opções
            opcao = int(input('Selecione uma opção: '))
        except ValueError: 
            print(f'Digite apenas números!')
            continue

        if opcao == 0: # sair do programa
            print('Encerrando Lista de Afazeres...')
            break
        if opcao not in opcoes: # se for selecionado outro número
            print('Opção não encontrada - Selecione uma opção válida.')
            continue

        opcoes[opcao]()

carregar_tarefas()
menu()