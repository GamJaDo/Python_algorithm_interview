class CircularDeque:
    def __init__(self, k):
        self.k = k
        self.deque = [None] * k
        self.front = 0
        self.rear = 0
        self.size = 0

    def insertFront(self, value):
        if self.isFull():
            return False
        self.front = (self.front - 1) % self.k
        self.deque[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        self.deque[self.rear] = value
        self.rear = (self.rear + 1) % self.k
        self.size += 1
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        self.deque[self.front] = None
        self.front = (self.front + 1) % self.k
        self.size -= 1
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % self.k
        self.deque[self.rear] = None
        self.size -= 1
        return True

    def getFront(self):
        return self.deque[self.front] if not self.isEmpty() else -1

    def getRear(self):
        return self.deque[(self.rear - 1) % self.k] if not self.isEmpty() else -1

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.k


# 원형 데크 생성 (크기 3)
circular_deque = CircularDeque(3)

# 원형 데크에 원소 추가
circular_deque.insertLast(1)
circular_deque.insertLast(2)
circular_deque.insertFront(3)

# 원형 데크의 내용 확인
print(circular_deque.getFront())  # 3
print(circular_deque.getRear())   # 2

# 원형 데크에서 원소 삭제
circular_deque.deleteLast()

# 원형 데크의 내용 확인
print(circular_deque.getFront())  # 3
print(circular_deque.getRear())   # 1
