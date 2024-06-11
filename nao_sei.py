import time

def myFunc():
    start_time = time.time()  # Marca o tempo de início
    s = 0  # Inicializa a variável s com 0
    for i in range(1, n + 1):  # Loop que vai de 1 até n (incluindo n)
        s = s + 1  # Incrementa s em 1 a cada iteração

    end_time = time.time()  # Marca o tempo de término
    return s, end_time - start_time  # Retorna o valor de s e o tempo total gasto

n = 5
print(myFunc())  # Chama a função e imprime o resultado