# CALCULADORA SIMPLES
# Objetivo com o código: Receber dois números, realizar uma operação e mostrar o resultado.
loop = 0
while loop == 0:
    operacao = int(input('Selecione a operação que deseja:\n1 - Adição | 2 - Subtração | 3 - Multiplicação | 4 - Divisão | 5 - Potencia:\n'))
    numero = float(input('Digite o primeiro número desejado: '))
    numero2 = float(input('Digite o segundo número desejado: '))

    if operacao == 1:
        soma = numero + numero2
        print(f'A adição dos números é de: {soma}.')
    elif operacao == 2:
        subtracao = numero - numero2
        print(f'A subtração dos números é de: {subtracao}')
    elif operacao == 3:
        multiplicacao = numero * numero2
        print(f'A multiplicação dos números é de: {multiplicacao}')
    elif operacao == 4:
        if numero2 == 0:
            print('Erro: Divisão por 0 não é permitida.')
        else:
            divisao = numero / numero2
            print(f'A divisão dos números é de: {divisao}')
    elif operacao == 5:
        potencia = numero ** numero2
        print(f'A potência dos números é de: {potencia}')
    else:
        print('Operação selecionada inválida, tente novamente.')
    
    rep = int(input('Deseja continuar? 1 - Sim | 2 - Não\n'))
    if rep == 2:
        loop += 1