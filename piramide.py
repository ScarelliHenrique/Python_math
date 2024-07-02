#Sua tarefa é escrever um programa que lê o número de blocos que os construtores têm e gera a altura da pirâmide que pode ser construída 
#usando esses blocos.

#Nota: a altura é medida pelo número de camadas totalmente concluídas; se os construtores não tiverem um número suficiente de blocos e 
#não puderem concluir a próxima camada, eles terminarão seu trabalho imediatamente.

blocks = int(input("Insira o número de blocos:"))  
i= 1
a=0


while blocks>=i:
    blocks=blocks-i
    i+=1
    a+=1
else:
    
    print(f"A altura da pirâmide é {a} blocos de altura ")
    print(f'Sobraram {blocks} blocos que não foram utilizados para a criação da piramide')