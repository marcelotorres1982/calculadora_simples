# Definindo funções básicas

# Adição
def adicao (a, b):
    return a + b

# Subtração
def subtracao(a, b):
    return a - b

# Multiplicação
def multiplicacao(a, b):
    return a * b

# Divisão
def divisao(a, b):
    return a / b

# Definindo função para efetuar o cálculo, a partir da interação do usuário

def calcular():
    numero1 = float(input('Digite o primeiro número: '))
    operacao = input('Selecione a operação (+, -, *, /): ')
    numero2 = float(input('Digite o segundo número: '))
    
    if operacao == '+':
        somar = adicao(numero1, numero2)
        print('O resultado da adição é :', somar)
    
    elif operacao == '-':
        subtrair = subtracao(numero1, numero2)
        print('O resultado da subtração é :', subtrair)
        
    elif operacao == '*':
        multiplicar = multiplicacao(numero1, numero2)
        print('O resultado da multiplicação é :', multiplicar)
        
    elif operacao == '/':
        dividir = divisao(numero1, numero2)
        print('O resultado da divisão é: ', dividir)
    
    else:
        print('Operação inválida')

calcular()