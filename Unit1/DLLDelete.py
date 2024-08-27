class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def delete_at_start(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_at_end(self):
        if self.tail is None:
            print("List is empty")
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def delete_in_middle(self, position):
        if self.head is None:
            print("List is empty")
            return

        if position == 0:
            self.delete_at_start()
            return

        current = self.head

        for _ in range(position):
            if current is None:
                print("Position out of bounds")
                return
            current = current.next

        if current == self.tail:
            self.delete_at_end()
        else:
            current.prev.next = current.next
            current.next.prev = current.prev

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
