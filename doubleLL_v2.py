class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """
        Appends a new node with the given data to the end of the doubly linked list.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur

    def prepend(self, data):
        """
        Prepends a new node with the given data to the beginning of the doubly linked list.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def print_list(self):
        """
        Prints the data of each node in the doubly linked list.
        """
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
    

slinky = DoublyLinkedList()

slinky.append(1)
slinky.append(2)
slinky.append(3)
slinky.append(4)

slinky.prepend(5)

slinky.print_list()