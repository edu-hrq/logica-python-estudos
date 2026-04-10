# CALCULADORA SIMPLES
# Objetivo com o código: Receber dois números, realizar uma operação e mostrar o resultado.
loop = 0
while loop == 0:
    print('\n======== CALCULADORA ========')
    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Potenciação')
    print('- 0 Sair')
    print('=============================')
    operacao = int(input('Escolha uma opção: '))

    if operacao == 0: # opção p/ sair da calculadora
        print('Encerrando calculadora...')
        break

    if operacao < 0 or operacao > 5: # validação antes de pedir números
        print('Opção inválida! Tente novamente.')
        continue

    numero = float(input('Digite o primeiro número desejado: '))
    numero2 = float(input('Digite o segundo número desejado: '))

    if operacao == 1:
        print(f'A adição dos números é de: {numero + numero2}.')
    elif operacao == 2:
        print(f'A subtração dos números é de: {numero - numero2}')
    elif operacao == 3:
        print(f'A multiplicação dos números é de: {numero * numero2}')
    elif operacao == 4:
        if numero2 == 0:
            print('Erro: Divisão por 0 não é permitida.')
        else:
            print(f'A divisão dos números é de: {numero / numero2}')
    elif operacao == 5:
        print(f'A potência dos números é de: {numero ** numero2}')
    else:
        print('Operação selecionada inválida, tente novamente.')