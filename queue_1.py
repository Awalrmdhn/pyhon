class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.rear = None

    def empty(self):
        return self.head is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.head = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
            
    def dequeue(self):
        if self.head is None:
            raise Exception("Queue kosong")
        else:
            temp = self.head
            self.head = self.head.next
            return temp.data

    def swap(self, index1, index2):
        if index1 == index2:
            return

        prev1 = None
        cur1 = self.head
        for _ in range(index1):
            prev1 = cur1
            cur1 = cur1.next

        prev2 = None
        cur2 = self.head
        for _ in range(index2):
            prev2 = cur2
            cur2 = cur2.next

        if prev1:
            prev1.next = cur2
        else:
            self.head = cur2

        if prev2:
            prev2.next = cur1
        else:
            self.head = cur1

        cur1.next, cur2.next = cur2.next, cur1.next

        if cur1.next is None:
            self.rear = cur1
        elif cur2.next is None:
            self.rear = cur2

    def head_item(self):
        if not self.empty():
            return self.head.data
        else:
            raise Exception("Queue kosong")

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

queue = Queue() 
while (1):
    queue.print_list()
    print("\n\n1. Enqueue")
    print("2. Dequeue")
    print("3. Swap")
    print("4. Exit")
    print("================================")
    print(" ")
    pilih = int(input("Masukkan pilihan: "))
    if pilih == 1:
        data = input("Masukkan data: ")
        queue.enqueue(data)
    elif pilih == 2:
        queue.dequeue()
    elif pilih == 3:
        index1 = int(input("Masukkan index pertama: "))
        index2 = int(input("Masukkan index kedua: "))
        queue.swap(index1, index2)
    elif pilih == 4:
        break
    else:
        print("Pilihan salah")

# queue.enqueue(10)
# queue.enqueue(20)
# queue.enqueue(30)
# queue.enqueue(40)

# queue.push(50)

# queue.print_list()

# print("================================")

queue.pop()

# queue.swap(3,1)

queue.print_list()