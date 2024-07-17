class Nodo:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
    
class FilaEncadeada:
    def __init__(self) -> None:
        self.inicio = None
        self.fim = None
    
    def inserir(self, dado):
        novo = Nodo(dado)
        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo
    
    def consultar(self):
        if self.inicio is None:
            return None
        return self.inicio.dado


    def remover(self):
        if self.inicio is not None:
            self.inicio = self.inicio.proximo
            if self.inicio is None:
                self.fim = None
    
    def consultar(self):
        if self.inicio is None:
            return None
        return self.inicio.dado
    
    def printar(self):
        atual = self.inicio
        while atual is not None:
            print(atual.dado, end=" ")
            atual = atual.proximo
        print()

fila = FilaEncadeada()
fila.inserir(1)
fila.inserir(2)
fila.inserir(3)

fila.printar()

print("Remover 2 itens")

fila.remover()
fila.remover()

fila.printar()