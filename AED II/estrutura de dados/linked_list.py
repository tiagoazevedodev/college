class Node:
    def __init__(self, info):
        self.info = info
        self.next = None


class LinkedList:
    def __init__(self):
        self.start = None
        self.lenght = 0

    def search(self, info):
        """Retorna o índice do nó que contém o valor passado por parâmetro."""
        aux = self.start
        cont = 0

        while aux is not None:
            if aux.info == info:
                return cont
            cont += 1
            aux = aux.next

        return False

    def print(self):
        """Retorna todos os itens da lista encadeada separados por ' '."""
        aux = self.start
        saida = ""
        while aux is not None:
            saida += " " + str(aux.info)
            aux = aux.next
        return saida

    def insert(self, info):
        """Insere um item no fim da lista encadeada."""
        self.lenght += 1
        aux = self.start
        if aux is None:
            self.start = Node(info)
            return True
        while aux is not None:
            if aux.next is None:
                aux.next = Node(info)
                return True
            aux = aux.next
        
        
    def delete(self, info):
        """Deleta o primeiro valor encontrado na lista encadeada."""
        aux = self.start
        while aux is not None:
            if aux.info == info:
                aux.next = aux.next.next
                return True
            aux = aux.next
        raise ValueError("Value not found")

    
    def index(self, index):
        """Retorna o valor do nó do index passado por parâmetro."""
        if index < 0 or index >= self.lenght:
            raise IndexError("Index out of range")
        
        aux = self.start
        cont = 0 
        while aux is not None:
            if cont == index:
                return aux.info
            cont += 1
            aux = aux.next
