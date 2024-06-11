def calcular_mdc():
    a = int(input('Insira um valor: '))
    b = int(input('Insira outro valor: '))
    
    def mdc(a, b):
        while b:
            a, b = b, a % b
        return a

    resultado = mdc(a, b)
    print("O MDC dos valores inseridos é:", resultado)

calcular_mdc()