print('Em qual escala está a temperatura que você quer converter?')
print('Digite C para Celsius, F para Fahrenheit e K para Kelvin')
escolha = input('Qual é a escala atual da temperatura? ').strip().upper()
temperatura = float(input('Qual é o valor da temperatura na escala atual? '))

print('Para qual escala você quer converter a temperatura?')
conversao = input().strip().upper()

if escolha == "C" and conversao == "K":
    print('A temperatura em Kelvin é:', temperatura + 273.15, 'K')
elif escolha == "C" and conversao == "F":
    print('A temperatura em Fahrenheit é:', (temperatura * 9/5) + 32, 'F')
elif escolha == "K" and conversao == "C":
    print('A temperatura em Celsius é:', temperatura - 273.15, 'C')
elif escolha == "K" and conversao == "F":
    print('A temperatura em Fahrenheit é:', (temperatura - 273.15) * 9/5 + 32, 'F')
elif escolha == "F" and conversao == "C":
    print('A temperatura em Celsius é:', (temperatura - 32) * 5/9, 'C')
elif escolha == "F" and conversao == "K":
    print('A temperatura em Kelvin é:', (temperatura - 32) * 5/9 + 273.15, 'K')
else:
    print('Conversão inválida. Por favor, verifique as escalas e tente novamente.')