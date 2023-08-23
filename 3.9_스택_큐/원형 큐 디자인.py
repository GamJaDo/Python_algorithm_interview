class MyCircularQueue:
    def __init__(self, k):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0
        self.p2 = 0

    def enQueue(self, value):
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2+1) % self.maxlen

            return True
        else:
            return False

    def deQueue(self):
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1+1) % self.maxlen

            return True

    def Front(self):
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def Rear(self):
        return -1 if self.q[self.p2-1] is None else self.q[self.p2-1]

    def isEmpty(self):
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self):
        return self.p1 == self.-p2 and self.q[self.p1] is None

"""
MAX_QSIZE = 10

class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_QSIZE

    def isEmpty(self):
        return self.front == self.rear
    def isFull(self):
        return self.front == (self.rear+1) % MAX_QSIZE
    def clear(self):
        self.front = self.rear

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear+1) % MAX_QSIZE
            self.items[self.rear] = item

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1) % MAX_QSIZE
            return self.items[self.front]

    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front + 1) % MAX_QSIZE]

    def size(self):
        return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE

    def display(self):
        out = []
        
        if self.front < self.rear:
            out = self.items[self.front+1:self.rear+1]
        else:
            out = self.items[self.front+1:MAX_QSIZE] + self.items[0:self.rear+1]
            
        print("[f=%s,r=%d] ==> " % (self.front, self.rear), out)
"""
