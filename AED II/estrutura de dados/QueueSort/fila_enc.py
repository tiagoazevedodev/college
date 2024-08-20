class Nodo:
    def __init__(self, valor):
        self.info = valor
        self.prox = None
        
class Fila:
    def __init__(self):
        self.ini = None
        self.fim = None

    def inserir(self, valor):
        elem = Nodo(valor)
        if self.ini == None and self.fim == None:
            self.ini = elem
        else:
            self.fim.prox = elem
        self.fim = elem

    def consultar(self):
        if self.ini != None:
            return self.ini.info
        else:
            return None
    
    def remover(self): # Fila só remove do INICIO
        if self.ini != None:
            self.ini = self.ini.prox
            if self.ini == None:
                self.fim = None
    
    def printar(self):
        atual = self.ini
        while atual != None:
            print(atual.info, end=" ")
            atual = atual.prox
        print()

    def vazia(self):
        if self.ini == None:
            return True
        return False
