def merge(A, p, q, r):
    n1 = q - p + 1  # Número de elementos do primeiro sub-vetor
    n2 = r - q  # Número de elementos do segundo sub-vetor
    
    L = []  # Inicializando os vetores L e R
    R = []
    
    for i in range(n1):
        L.append(A[p + i])  # Preenchendo o vetor L com os elementos do primeiro sub-vetor
    
    for j in range(n2):
        R.append(A[q + j + 1])  # Preenchendo o vetor R com os elementos do segundo sub-vetor
    
    L.append(float('inf'))  # Adicionando um valor infinito no fim de L e R
    R.append(float('inf'))
    
    i = 0
    j = 0
    
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)
    return A


A = [67, 3423, 8, 987, 6543, 23254, 5568, 87675654, 332, 2435, 6789]

print(merge_sort(A, 0, len(A) - 1))
