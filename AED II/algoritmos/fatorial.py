n = int(input("Qual valor voc^e deseja calcular o fatorial? "))

def fatorialIterativo(n):
    if n == 0:
        return 1
    elif n < 0:
        return "Valor inválido"
    for i in range(1, n+1):
        fatorial = fatorial * i

def fatorialRecursivo(n):
    if n == 0:
        return 1
    else:
        return n * fatorialRecursivo(n-1)
    
#print(fatorialRecursivo(n))
print(fatorialIterativo(n))
