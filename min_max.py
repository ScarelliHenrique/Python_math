n = int(input('Quantos valores você deseja digitar? '))
numero = []

for i in range(n):
    while True:
        try:
            valor = int(input(f'Digite o {i+1}° valor: '))
            numero.append(valor)
            break  
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

print("\nO maior valor é:", max(numero))
print('')
print("O menor valor é:", min(numero))