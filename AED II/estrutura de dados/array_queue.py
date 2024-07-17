
class FilaContiguidade:
    def __init__(self, maximo):
        self.maximo = maximo
        self.inicio = None
        self.fim = None
        self.array = [None] * maximo
        self.tamanho = 0

    def inserir(self, dado):
        if self.inicio is None:
            self.inicio = 0
        elif self.tamanho < self.maximo:
            if self.inicio <= self.fim and self.fim < self.max - 1:
                self.fim += 1
            if self.ini <= self.fim and self.fim == self.max - 1:
                
        self.array[self.fim] = dado
        self.tamanho += 1
