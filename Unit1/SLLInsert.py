class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert_in_middle(self, data, position):
        new_node = Node(data)

        if position == 0:
            self.insert_at_start(data)
            return

        current = self.head

        for _ in range(position - 1):
            if current is None:
                print("Position out of bounds")
                return
            current = current.next

        if current is None or current.next is None:
            self.insert_at_end(data)
        else:
            new_node.next = current.next
            current.next = new_node

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


linked_list = SinglyLinkedList()
linked_list.insert_at_start(10)
linked_list.insert_at_end(20)
linked_list.insert_in_middle(15, 1) 
linked_list.insert_in_middle(25, 3)  
linked_list.insert_in_middle(5, 0)   
linked_list.display()
