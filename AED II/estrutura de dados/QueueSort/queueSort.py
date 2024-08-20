from random import randint
from pilha_encadeada import Pilha
from fila_enc import Fila

# Criação da fila com valores aleatórios para teste
fila = Fila()

for i in range(10):
    fila.inserir(randint(0, 100))

print("Fila desordenada:")
fila.printar()

def ordenar(fila, decrescente=False):
    pilhaAux = Pilha()
    pilhaOrdenada = Pilha()

    while not fila.vazia():
        # Fila ainda não está vazia
        elemento = fila.consultar()
        fila.remover() # Remove o elemento da fila
        
        while not pilhaOrdenada.vazia() and (pilhaOrdenada.consultar() <= elemento and decrescente): # Enquanto a pilha ordenada não estiver vazia e o elemento atual for menor que o topo da pilha
            # Enquanto a pilha ordenada não estiver vazia e o elemento atual for maior que o topo da pilha
            if decrescente:
                
            pilhaAux.empilhar(pilhaOrdenada.consultar())
            pilhaOrdenada.remover()
        
        pilhaOrdenada.empilhar(elemento) # Empilha o elemento atual pois ele é maior que o topo da pilha ordenada

        while not pilhaAux.vazia(): # Volta os elementos da pilha auxiliar para a pilha ordenada
            pilhaOrdenada.empilhar(pilhaAux.consultar())
            pilhaAux.remover()

    while not pilhaOrdenada.vazia():
        fila.inserir(pilhaOrdenada.consultar())
        pilhaOrdenada.remover()

print("Fila ordenada decrescente:")
ordenar(fila=fila)
fila.printar()

