class Node:
    def __init__(self, coeff, exp):
        self.coeff = coeff
        self.exp = exp
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def create(self, coeff, exp):
        new_node = Node(coeff, exp)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def display(self):
        temp = self.head
        poly = []
        while temp:
            poly.append(f"{temp.coeff}x^{temp.exp}")
            temp = temp.next
        print(" + ".join(poly))

    def add(self, other):
        p1 = self.head
        p2 = other.head
        result = LinkedList()
        while p1 and p2:
            if p1.exp > p2.exp:
                result.create(p1.coeff, p1.exp)
                p1 = p1.next
            elif p1.exp < p2.exp:
                result.create(p2.coeff, p2.exp)
                p2 = p2.next
            else:
                sum_coeff = p1.coeff + p2.coeff
                if sum_coeff != 0:
                    result.create(sum_coeff, p1.exp)
                p1 = p1.next
                p2 = p2.next
        
        while p1:
            result.create(p1.coeff, p1.exp)
            p1 = p1.next

        while p2:
            result.create(p2.coeff, p2.exp)
            p2 = p2.next

        return result

# Input and usage
poly1 = LinkedList()
n = int(input())
for _ in range(n):
    coeff, exp = map(int, input().split())
    poly1.create(coeff, exp)
poly1.display()

poly2 = LinkedList()
m = int(input())
for _ in range(m):
    coeff, exp = map(int, input().split())
    poly2.create(coeff, exp)
poly2.display()

result = poly1.add(poly2)
result.display()
