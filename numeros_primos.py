def num_primo_linear(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    else:
        return True
    
def num_primo_recursiva(x, i):
    if i == x:
        return True
    elif x % i == 0:
        return False
    else:
        return num_primo_recursiva(x, i + 1)
    
def lista_primos_recursiva(n):
    if n == 2:
        return [2]
    else:
        lista_menor = lista_primos_recursiva(n - 1)
        if num_primo_recursiva(n, 2) == True:
            return lista_menor + [n]
        else:
            return lista_menor
        
def lista_primos_linear(n):
    lista_primos = []
    for candidato in range(2, n + 1):
        if num_primo_linear(candidato) == True:
            lista_primos.append(candidato)
    return lista_primos
            
funcao = input("Com qual função gostaria de verificar se o número é primo? Recursiva ou Linear? ")

while True:
    try:
        numero = int(input("Digite o número que gostaria de verficar se é primo: "))
        if numero < 0: # Caso o usuário escolha uma posição invalida, pede para reescrever uma posição valida
            print("Posição invalida!")
            continue
        break
    except:
        print(("Caractere invalido, digite um número!")) # Caso o usuário digite uma letra na posição, pede para reescrever

while numero <= 1: # Verifica se o usuário escreveu um número maior que 1
    numero = int(input("O número precisa ser maior que 1, digite novamente: "))

while funcao.lower() != "linear" and funcao.lower() != "recursiva": # Verifica se o nome das funções foram escritos corretamente
    funcao = input("Função invalida! Escolha entre Recursiva ou Linear: ")
    
if funcao.lower() == "linear": # Acontece aqui a requisição da função
    print(f"p({numero}) = {lista_primos_linear(numero)}")
else:
    print(f"p({numero}) = {lista_primos_recursiva(numero)}")
