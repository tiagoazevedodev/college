class Node:
    def __init__(self, info):
        self.info = info
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.start = None
        self.end = None
        self.length = 0
            
    def insert(self, info, index):
        if index > self.length:
            raise IndexError("Index out of range")
        elif self.start is None:
            self.start = Node(info)
            self.end = self.start
        else:
            middle = self.end - self.start + 1 
            if index <= middle:
                current = self.start
                for _ in range(index):
                    current = current.next
                new_node = Node(info)
                new_node.next = current.next
                current.next = new_node
            else:
                current = self.end
                for _ in range(middle, index):
                    current = current.next
                new_node = Node(info)
                new_node.next = current.next
                current.next = new_node
                self.end = new_node
        self.length += 1
        
    def remove(self, index):
        if index >= self.length:
            raise IndexError("Index out of range")
        
        current = self.start
        if index == 0:
            self.start = self.start.next
        else:
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.length -= 1
    
    def position(self, info):
        pass
    
    def value(self, index):
        pass
    
    def destroy(self):
        pass
    
    def show(self):
        string = ""
        current = self.start
        while current is not None:
            string += str(current.info) + ", "
            current = current.next
        return string
    
lista = LinkedList()

lista.insert(1, 0)
lista.insert(2, 4)
print(lista.show())
