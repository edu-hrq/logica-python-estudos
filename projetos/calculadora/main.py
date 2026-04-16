# CALCULADORA SIMPLES - Objetivo com o código: Receber dois números, realizar uma operação e mostrar o resultado.
historico = []

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
def visu_historico():
      print('HISTÓRICO:')
      if not historico:
        print('Histórico vazio - Nenhuma operação realizada')
      else:
        for item in historico:
            print(item)
    
operacoes = { # dicionario das operacoes que serão feitas na calculadora
        1: adicao,
        2: subtracao,
        3: multiplicacao,
        4: divisao,
        5: potenciacao,
        6: visu_historico,
    }

simbolos = {
      1: '+',
      2: '-',
      3: '*',
      4: '/',
      5: '**',  
    }

while True:
    print('\n======== CALCULADORA ========\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Potenciação\n6 - Ver histórico\n7 - Limpar histórico\n0 - Sair\n=============================')
    try:
        operacao = int(input('Escolha uma opção: '))
    except ValueError:
        print('Digite apenas números!')
        continue

    if operacao == 0: # opção p/ sair da calculadora
        print('Encerrando calculadora...')
        break

    if operacao == 7: # limpar o histórico
          historico.clear()
          print('Histórico apagado!')
          continue
    
    if operacao not in operacoes:
         print('Operação inválida! Tente novamente: ')
         continue
    
    try: # emtrada de dados
        numero = float(input('Digite o primeiro número desejado: '))
        numero2 = float(input('Digite o segundo número desejado: '))
    except ValueError:
          print('Digite valores numéricos!')
          continue
    
    resultado = operacoes[operacao](numero, numero2) # processamento dos dados

    simbolo = simbolos[operacao] # guarda a operação selecionada
    historico.append(f'{numero} {simbolo} {numero2} = {resultado}') # adiciona cálculo feito ao histórico
    
    print(f'\nResultado da operação desejada: {resultado}\n') # imprime o resultado dos dados