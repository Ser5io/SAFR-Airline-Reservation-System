import Node 
        
class Linked_list:
    def __init__(self):
        self.head = self.tail = None
        self.counter = 0
    
    def isEmpty(self):
        return self.counter == 0
    # Adds a new node at the beginning of the list.
    def add(self, data):
        newNode = Node(data)
        
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
            
        self.counter += 1
    
    def append(self, data):
        pass
    
    def insert(self, data, pos):
        pass
    
    def search(self, data):
        pass
    
    def traverse(self):
        pass
    
    # Removes the head node and decrements the counter.
    def removeHead(self):
        if self.isEmpty():
            return
        
        temp = self.head
        self.head = self.head.next
        temp = temp.prev = temp.next = None
        self.counter -= 1
    
    def removeTail(self):
        pass
    
    def removeAtItem(self, data):
        pass
    
    def clear(self):
        pass
    
    def removeAll(self, data):
        pass