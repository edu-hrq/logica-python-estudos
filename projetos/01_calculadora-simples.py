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

    numero = float(input('Digite o primeiro número desejado: '))
    numero2 = float(input('Digite o segundo número desejado: '))

    if operacao == 1:
        print(f'A adição dos números é de: {adicao(numero, numero2)}.')
    elif operacao == 2:
        print(f'A subtração dos números é de: {subtracao(numero, numero2)}')
    elif operacao == 3:
        print(f'A multiplicação dos números é de: {multiplicacao(numero, numero2)}')
    elif operacao == 4:
        print(f'A divisão dos números é de: {divisao(numero, numero2)}')
    elif operacao == 5:
        print(f'A potência dos números é de: {potenciacao(numero, numero2)}')
    else:
        print('Operação selecionada inválida, tente novamente.')