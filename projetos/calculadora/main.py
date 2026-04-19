# CALCULADORA SIMPLES - Objetivo com o código: Receber dois números, realizar uma operação e mostrar o resultado.
from datetime import datetime

historico = []

def obter_data_e_hora(): # função para obter data e hora da operação feita
     return datetime.now().strftime('%d/%m/%Y %H:%M:%S')
def adicao(a, b): # função de adição
        return a + b
def subtracao(a, b): # função de subtração
        return a - b
def multiplicacao(a, b): # função de multiplicação
        return a * b
def divisao(a, b): # função de divisão (que valida se o divisor é 0 ou não)
        if b == 0:
            return "Erro: Divisão por 0 não é permitida."
        else:
            return a / b
def potenciacao(a, b): # função de potenciação
        return a ** b
def ver_historico(): # função de visualização de histórico
    if not historico:
        print('Histórico vazio - Nenhuma operação realizada')
    else:
        for item in historico:
            print(item)
def limpar_historico(): # função de exclusão de histórico
    resposta = input('Tem certeza de que deseja limpar o histórico? Digite S para Sim ou N para Não: ').strip().lower()
    if resposta and resposta[0] == 's':
        historico.clear()
        print('Histórico apagado!')
    else:
         print('Histórico não apagado.')

operacoes = { # dicionario das operacoes que serão feitas na calculadora
        1: adicao,
        2: subtracao,
        3: multiplicacao,
        4: divisao,
        5: potenciacao,
        6: ver_historico,
        7: limpar_historico,
    }

simbolos = {
      1: '+',
      2: '-',
      3: '*',
      4: '/',
      5: '**',  
    }

while True:
    print('======== CALCULADORA ========\n'
          '1 - Adição\n'
          '2 - Subtração\n'
          '3 - Multiplicação\n'
          '4 - Divisão\n'
          '5 - Potenciação\n'
          '6 - Ver histórico\n'
          '7 - Limpar histórico\n'
          '0 - Sair\n'
          '=============================')
    try:
        operacao = int(input('Escolha uma opção: '))
    except ValueError:
        print('Digite apenas números!')
        continue

    if operacao == 0: # opção p/ sair da calculadora
        print('Encerrando calculadora...')
        break
    
    if operacao not in operacoes:
         print('Operação inválida! Tente novamente: ')
         continue
    
    if operacao == 6:
         ver_historico()
         continue

    if operacao == 7:
         limpar_historico()
         continue

    try: # entrada de dados
        numero = float(input('Digite o primeiro número desejado: '))
        numero2 = float(input('Digite o segundo número desejado: '))
    except ValueError:
          print('Digite valores numéricos!')
          continue
    
    resultado = operacoes[operacao](numero, numero2) # processamento dos dados

    simbolo = simbolos[operacao] # guarda a operação selecionada
    historico.append(f'[{obter_data_e_hora()}] {numero} {simbolo} {numero2} = {resultado}') # adiciona cálculo feito ao histórico
    
    print(f'Resultado da operação desejada: {resultado}\n') # imprime o resultado dos dados