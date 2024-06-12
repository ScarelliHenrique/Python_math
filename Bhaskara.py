#equação de Bhaskara
import math 

a=int(input('Digite o valor de A:'))
b=int(input('Digite o valor de B:'))
c=int(input('Digite o valor de C:'))

delta=b*b-4*a*c

if(delta<0):
    print('Não tem raízes reais')
elif(delta==0):
    x=-b/(2*a)
    print("temops como solução duas raizes reais e iguais a:", x)
else:
    x1= (-b+math.sqrt(delta))/(2*a)
    x2= (-b-math.sqrt(delta))/(2*a)
    print('temos como solução duas raizes reais e diferentes')
    print ('x1=', x1)
    print ('x2=', x2)
