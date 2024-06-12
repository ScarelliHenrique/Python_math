#verifica se o numero é primo
num=9

for i in range(2,num):
    if num % i ==0:
        print(f'The number {num} is not Prime')
        break
else:
        print(f'The number {num} is Prime')
