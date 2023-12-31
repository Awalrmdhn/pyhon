class node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
        
class lankly:
    def __init__ (self):
        self.head = node()
        
    def append (self,data):
        new_node = node(data)
        cur = self.head 
        while cur.next!=None:
            cur=cur.next
        cur.next = new_node
        
    def length (self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur .next
        return total 
    
    def display(self):
        elms = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elms.append(cur_node.data)
        print (elms)
        
    def get(self, index):
        if index >= self.length():
            print ("ERROR: 'get' index out of range!")
            return None
        cur_idx = 0
        cur_node = self.head  
        while True:
            cur_node = cur_node.next
            if cur_idx == index : return cur_node.data
            cur_idx+=1
            
    def erase(self, index):
        if index >= self.length():
            print ("hapus nya kebanyakan")
            return
        cur_idx = 0
        cur_node = self.head 
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx+=1
            
my_list = lankly()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

my_list.display()

print("\nberikut adalah contoh pengguana get\n")
print("elemen ke 3 adalah %d" % my_list.get(2))

print(f"elemen ke 2 adalah {my_list.get(1)}")

print ('\nsetelah di hapus pada index ke 2 maka akan menghasilkan hasil sbg berikut')

my_list.erase(2)

my_list.display()