class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class duoblelinky:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = node(data)
        if self.head is None:
            new_node.prev = None
            self.head = new_node
        else:   
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node 
            new_node.prev = cur
            new_node.next = None
    
    def prepend (self, data):
        new_node = node(data)
        if self.head is None:
            new_node.prev = None
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head  
            self.head = new_node
            new_node.prev = None
            
    def print_list(self):
        cur = self.head 
        while cur:
            print (cur.data)
            cur = cur.next
    

slinky = duoblelinky()


slinky.append(1)
slinky.append(2)
slinky.append(3)
slinky.append(4)

slinky.prepend(7)

slinky.print_list()