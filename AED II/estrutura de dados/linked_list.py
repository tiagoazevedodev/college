
class LinkedList:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def buscar(self, valor):
        aux = self.inicio
        cont = 0

        while aux is not None:
            if aux.valor == valor:
                return cont
            cont += 1
            aux = aux.prox

        return False

    def imprimir(self):
        aux = self.inicio
        
        while aux is not None:
            saida += " " + aux.valor
            aux = aux.prox

    def inserir(self, valor):
        pass
        
    def remover(self, valor):
        pass

    def index(self, valor):
        aux = self.inicio
        cont = 0
        while aux is not None:
            if aux.valor == valor:
                return cont
            cont += 1
            aux = aux.prox


minhaLista = LinkedList()

minhaLista.buscar(2)