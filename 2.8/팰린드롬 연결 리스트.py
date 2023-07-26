import collections

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

    """
    def isPalindrome(self):
        dq = collections.deque()
        if not self.head:
            return True

        node = self.head
        while node is not None:
            dq.append(node.val)
            node = node.next

        while len(dq) > 1:
            if dq.popleft() != dq.pop():
                return False

        return True
    """
    def isPalindrome(self):
        rev = None
        slow = fast = self.head

        while fast and fast.next:
            fast = fast.next.next
            if fast != None:
                print("fast: ", fast.val)

            rev, rev.next, slow = slow, rev, slow.next
            print("slow1: ", slow.val)
            print("rev1: ", rev.val)
            if rev.next != None:
                print("rev1.next: ", rev.next.val)
        if fast:
            slow = slow.next
            print("if: ", slow.val)
        print("======================================")
        print(slow.next.val)
        print("======================================")
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
            if slow != None:
                print("slow2: ", slow.val)
            else:
                print("sf")
            if rev !=  None:
                print("rev2: ", rev.val)
            else:
                print("rf")
        return not rev
    
    def display(self):
        n = self.head
        while n != None:
            print(n.val, end = ' -> ')
            n = n.next
        print("None")
        
s = LinkedStack()

s.push(1)
s.push(2)
s.push(3)
s.push(3)
s.push(2)
s.push(1)

print(s.isPalindrome())
