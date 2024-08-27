class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head

    def insert_in_middle(self, data, position):
        new_node = Node(data)

        if position == 0:
            self.insert_at_start(data)
            return

        current = self.head

        for _ in range(position - 1):
            if current.next == self.head:
                return
            current = current.next

        new_node.next = current.next
        current.next = new_node

        if current == self.tail:
            self.tail = new_node

    def display(self):
        if self.head is None:
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print(f"{self.head.data} (head)")


circular_linked_list = CircularSinglyLinkedList()
circular_linked_list.insert_at_start(10)
circular_linked_list.insert_at_end(20)
circular_linked_list.insert_in_middle(15, 1)
circular_linked_list.insert_in_middle(25, 3)
circular_linked_list.insert_in_middle(5, 0)
circular_linked_list.display()
