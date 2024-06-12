#programa que le numeros do teclado ate o usuario digitar 0 (zero)

#inicialmente esse era o codigo
#x=1
#while(x!=0):
#    x=int(input('Digite um numero: '))
#    print(x)

#print('Acabou, voce digitou ZERO')

#melhorei o codigo
while True:
    try:
        x = int(input('Digite um número (ou 0 para sair): '))
        if x == 0:
            break
        print(f'Você digitou: {x}')
    except ValueError:
        print('Entrada inválida! Por favor, digite um número válido.')

print('Acabou, você digitou ZERO.')