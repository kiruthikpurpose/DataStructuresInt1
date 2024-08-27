class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def delete_at_start(self):
        if self.head is None:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head

    def delete_at_end(self):
        if self.head is None:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next

            current.next = self.head
            self.tail = current

    def delete_in_middle(self, position):
        if self.head is None:
            return

        if position == 0:
            self.delete_at_start()
            return

        current = self.head

        for _ in range(position - 1):
            if current.next == self.head:
                return
            current = current.next

        if current.next == self.tail:
            self.delete_at_end()
        else:
            current.next = current.next.next

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