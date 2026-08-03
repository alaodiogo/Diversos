def fibbo_linear(x):
    fibbo_a = 0 # Caso base
    fibbo_b = 1 # Caso base
    resultado = 0
    if x == 0:
        return 0
    elif x == 1:
        return 1
    for i in range(x - 1):
        resultado = fibbo_a + fibbo_b
        fibbo_a = fibbo_b
        fibbo_b = resultado
    return resultado

def fibbo_recursiva(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibbo_recursiva(x-1) + fibbo_recursiva(x-2)

modo = input("Qual modo gostaria de resolver o Fibonacci? Recursiva ou Linear? ") # O usuário escolhe qual função usar

while modo.lower() != "linear" and modo.lower() != "recursiva": # Verifica se a função está escrita corretamente, caso não, pede para o usuário reescrever
    modo = input("Função invalida! Escolha entre Recursiva ou Linear: ")
    
while True:
    try:
        posicao_fibbo = int(input("Digite qual posição gostaria de saber: "))
        if posicao_fibbo < 0: # Caso o usuário escolha uma posição invalida, pede para reescrever uma posição valida
            print("Posição invalida!")
            continue
        break
    except:
        print(("Caractere invalido, digite um número!")) # Caso o usuário digite uma letra na posição, pede para reescrever
    
if modo.lower() == "linear": #Aqui acontece a escolha da função e sua invocação para o cálculo
    print(fibbo_linear((posicao_fibbo)))
else:
    print(fibbo_recursiva((posicao_fibbo)))