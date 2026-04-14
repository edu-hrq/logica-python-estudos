# CALCULADORA SIMPLES - Objetivo com o código: Receber dois números, realizar uma operação e mostrar o resultado.
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

operacoes = { # dicionario das operacoes que serão feitas na calculadora
        1: adicao,
        2: subtracao,
        3: multiplicacao,
        4: divisao,
        5: potenciacao,
    }

while True:
    print('\n======== CALCULADORA ========\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Potenciação\n0 - Sair\n=============================')
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
    
    numero = float(input('Digite o primeiro número desejado: '))
    numero2 = float(input('Digite o segundo número desejado: '))

    resultado = operacoes[operacao](numero, numero2)
    print(f'\nResultado da operação desejada: {resultado}\n')