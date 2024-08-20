class Nodo:
    def __init__(self, valor):
        self.info = valor
        self.prox = None

class Pilha:
    def __init__(self):
        self.topo = None

    def empilhar(self, dado):
        novo = Nodo(dado)
        if (not self.vazia()):
            novo.prox = self.topo
        self.topo = novo

    def remover(self):
        if (not self.vazia()):
            aux = self.topo
            self.topo = aux.prox
            return aux.info

    def consultar(self):
        if (not self.vazia()):
            return self.topo.info
        
    def destruir(self):
        while (not self.vazia()):
            self.Excluir()

    def vazia(self):
        return self.topo == None
    
    def printar(self):
        atual = self.topo
        while atual != None:
            print(atual.info, end=" ")
            atual = atual.prox
        print()
    
