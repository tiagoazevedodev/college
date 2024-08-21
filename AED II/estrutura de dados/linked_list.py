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

    def is_empty(self):
        return self.length == 0
            
    def insert(self, info, index):
        if index > self.length or index < 0:
            raise IndexError("Index out of range")
        new_node = Node(info)
        
        if self.is_empty():
            self.start = new_node
            self.end = new_node
        elif index == 0:  # Insert at the beginning
            new_node.next = self.start
            self.start.previous = new_node
            self.start = new_node
        elif index == self.length:  # Insert at the end
            self.end.next = new_node
            new_node.previous = self.end
            self.end = new_node
        else:  # Insert in the middle
            current = self.start
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            new_node.previous = current
            if current.next:
                current.next.previous = new_node
            current.next = new_node
        self.length += 1

    def append(self, info):
        self.insert(info, self.length)

    def remove(self, index):
        if index >= self.length or index < 0:
            raise IndexError("Index out of range")
        
        if index == 0:  # Remove from the beginning
            self.start = self.start.next
            if self.start:
                self.start.previous = None
            else:
                self.end = None
        elif index == self.length - 1:  # Remove from the end
            self.end = self.end.previous
            if self.end:
                self.end.next = None
            else:
                self.start = None
        else:  # Remove from the middle
            current = self.start
            for _ in range(index):
                current = current.next
            current.previous.next = current.next
            if current.next:
                current.next.previous = current.previous
        self.length -= 1

    def index_search_rec(self, node, info, index=0):
        # Base case: If node is None, the element is not in the list
        if node is None:
            return False
        # If the current node's info matches, return the index
        if node.info == info:
            return index
        # Recursively search in the next node until some base case is reached
        return self.index_search_rec(node.next, info, index + 1)

    def search(self, info):
        return self.index_search_rec(self.start, info)

    def reverse(self):
        current = self.start
        self.end = self.start
        previous = None
        while current is not None:
            next_node = current.next
            current.next = previous
            current.previous = next_node
            previous = current
            current = next_node
        self.start = previous
    
    def show(self):
        string = ""
        current = self.start
        while current is not None:
            string += str(current.info) + " -> "
            current = current.next
        return string.rstrip(" -> ")
    
# Use case
lista = LinkedList()
lista.append(0)
lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)
lista.append(10)
print(lista.show())  

print(lista.search(10))  # Output: 1 (index of element 4)
print(lista.search(6))  # Output: False (element 6 not found)
