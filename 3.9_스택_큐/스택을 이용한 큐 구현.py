class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek()
        
        return self.output.pop()

    def peek(self):
        if not self.output:
            while self.input():
                self.output.append(self.input.pop())

        return self.output[-1]

    def empty(self):
        return self.input==[] and self.output==[]
    
"""
from stack import Stack
s1 = Stack()
s2 = Stack()
def enqueue(val) :
    s1.push(val)
def dequeue() :
    if s2.isEmpty():
        while not(s1.isEmpty()):
            s2.push(s1.pop())
    return s2.pop()

enqueue(1)
enqueue(2)
enqueue(3)
print("dequeue() -->", dequeue())
print("dequeue() -->", dequeue())
enqueue(4);
enqueue(5);
print("dequeue() -->", dequeue())
print("dequeue() -->", dequeue())
"""
