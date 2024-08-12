const Merge = (A, p, q, r) => {
  n1 = q - p + 1; // Numero de elementos do primeiro subVetor
  n2 = r - q; // Numero de elementos do segundo subVetor
  let L = [] // Inicializando os vetores L e R
  let R = []
  for (let i = 0; i < n1; i++) {
    L[i] = A[p + i] // Preenchendo o vetor L com os elementos do primeiro subVetor
  }
  for (let j = 0; j < n2; j++) {
    R[j] = A[q + j + 1] // Preenchendo o vetor R com os elementos do segundo subVetor
  }

  L[n1] = Infinity // Adicionando um valor infinito no fim de L e R
  R[n2] = Infinity
  
  let i = 0
  let j = 0
  for (let k = p; k <= r; k++) {
    if (L[i] <= R[j]) {
      A[k] = L[i]
      i++
    } else {
      A[k] = R[j]
      j++
    }
  }
}


const MergeSort = (A, p, r) => {
  if (p < r) {
    let q = Math.floor((p + r) / 2)
    MergeSort(A, p, q)
    MergeSort(A, q + 1, r)
    Merge(A, p, q, r)
  }
  return A
}


const A = [67,3423,8,987,6543,23254,5568,87675654,332,2435,6789]

console.log(MergeSort(A, 0, A.length - 1))
