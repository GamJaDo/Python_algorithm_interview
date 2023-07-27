class Node:
    def __init__(self, elem, next=None):
        self.val = elem
        self.next = next

class LinkedStack:
    def __init__(self):
        self.head = None

    def push(self, item):
        n = Node(item, self.head)
        self.head = n

    def mergeTwoLists(self, l1: Node, l2: Node) -> Node:

        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l1, l2

        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1
    
    def display(self):
        n = self.head
        while n != None:
            print(n.val, end = ' -> ')
            n = n.next
        print("None")
        
s1 = LinkedStack()
s2 = LinkedStack()

s1.push(1)
s1.push(2)
s1.push(4)

s2.push(1)
s2.push(3)
s2.push(4)

print(s1.mergeTwoLists(s1, s2))
