def countingSort(A, B, K):
    n = len(A)
    for i in range(K + 1):
        B.append(0)
    for j in range(n):  
        B[A[j]] += 1
    for i in range(1, K + 1):
        B[i] += B[i - 1]
    C = []
    for i in range(n):
        C.append(0)
    for j in range(n - 1, -1, -1):
        B[A[j]] -= 1
        C[B[A[j]]] = A[j]
    return C
    