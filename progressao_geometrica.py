#formula progressao geometrica

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

pg = []

for n in range(10):
    termo = primeiro * (razao ** n)  # cálculo do n-ésimo termo da PG
    pg.append(termo)  # adiciona o termo à lista da PG

for termo in pg:
    print(termo, end=' -> ')
print('ACABOU')