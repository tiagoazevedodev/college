
class ArrayList:
    def __init__(self, capacidade:int):
        self.fim = None
        self.inicio = None
        self.capacidade = capacidade
        self.array = [None] * capacidade
    
    def buscar(self, valor):
        cont = 0
        for i in self.array:
            if i == valor:
                return cont
            cont += 1

    def imprimir(self):
        saida = ""
        for i in self.array:
            if i is not None:
                saida += " " + i
        print(saida)

    def inserir(self, valor):
        pass
        
    def remover(self, valor):
        pass


meuArray = ArrayList(10)
meuArray.imprimir()

