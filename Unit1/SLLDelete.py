class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
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

    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next

            current.next = None
            self.tail = current

    def delete_in_middle(self, position):
        if self.head is None:
            print("List is empty")
            return

        if position == 0:
            self.delete_at_start()
            return

        current = self.head

        for _ in range(position - 1):
            if current is None or current.next is None:
                print("Position out of bounds")
                return
            current = current.next

        if current.next == self.tail:
            self.delete_at_end()
        else:
            current.next = current.next.next

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
