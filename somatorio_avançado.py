#Esse codigo soma todos os numeros digitados pelo usuario 

n = int(input('Digite um número de valores a serem somados: '))
soma = 0  # Variável que acumula a soma
i = 0     # Contador de iterações

# Loop que continua até que i seja igual a n
while i < n:
    try:
        a = int(input(f'Digite o valor {i+1}: '))  # Solicita ao usuário um valor inteiro
        soma += a  # Adiciona o valor digitado à soma
        i += 1     # Incrementa o contador
    except ValueError:
        print('Entrada inválida! Por favor, digite um número válido.')

print(f'A soma dos {n} valores digitados é {soma}')
