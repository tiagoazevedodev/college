from linked_list import Node

class Stack():
    def __init__(self):
        """Inicializa uma instância de pilha."""
        self.top = None
        self.lenght = 0

    def push(self, info):
        """Insere um item no topo da pilha."""
        self.lenght += 1
        aux = Node(info)
        aux.next = self.top
        self.top = aux
        return True
    
    def pop(self):
        """Remove o último item da pilha e o retorna."""
        if self.top is None:
            raise ValueError("Empty stack")
        
        aux = self.top
        self.top = self.top.next
        self.lenght -= 1
        return aux.info

    def top(self):
        """Retorna o último item da pilha."""
        return self.top.info

    

pilha = Stack()

for i in range(10):
    pilha.push(i)
    
print(pilha.top.info)


