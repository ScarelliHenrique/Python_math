#somatorio  de todos os numeros digitados do 1 ate o N
n= int(input('Digite o valor de N: '))
i=1
soma=0
while (i<=n):
    soma=soma+i
    i=i+1
print(f'O valor da soma é {soma}')