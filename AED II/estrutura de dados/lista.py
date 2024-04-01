
class Lista:
    def __init__(self):
        self.inicio = None

    def imprimir(self):
        aux = self.inicio
        while aux is not None:
            print(aux.info)
            aux = aux.prox
    