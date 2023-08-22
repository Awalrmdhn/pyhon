class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if not self.empty():
            popped_item = self.head.data
            self.head = self.head.next
            return popped_item
        else:
            raise Exception("index kosong")

    def peek(self):
        if not self.empty():
            return self.head.data
        else:
            raise Exception("index kosong")
        
    def swap(self, index1, index2):
        if not self.empty():
            if index1 == 0:
                temp = self.head.data
                self.head.data = self.head.next.data
                self.head.next.data = temp
            else:
                cur = self.head
                for i in range(index1-1):
                    cur = cur.next
                temp = cur.next.data
                cur.next.data = cur.next.next.data
                cur.next.next.data = temp   
                return True
        else:
            raise Exception("index kosong")
        
        
    def print_list(self):
        if self.empty():
            print("Queue kosong")
            return
        cur = self.head
        data = ""
        while cur:
            data += str(cur.data)+ "->"
            cur = cur.next 
        print(data)

stack = Stack()
while True:
    stack.print_list()
    print("1. Push data")
    print("2. Pop data")
    print("3. Swap data")
    print("4. Exit")
    pilih = int(input("Pilih operasi: "))

    if pilih == 1:
        data = input("Masukkan data: ")
        stack.push(data)
    elif pilih == 2:
        popped_data = stack.pop()
        if popped_data is not None:
            print("Popped data:", popped_data)
        else:
            print("Stack is empty.")
    elif pilih == 3:
        index1 = int(input("Masukkan index pertama: "))
        index2 = int(input("Masukkan index kedua: "))
        if stack.swap(index1, index2):
            print("Data berhasil di swap")
            stack.print_list()
    elif pilih == 4:
        break
    else:
        print("Pilihan tidak valid.")

# stack.pop()
# stack.print_list()
# print("head item:", stack.peek())  

# stack.pop(20)
# print("head item after pop:", stack.peek()) 