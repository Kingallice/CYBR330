class DoubleEndedQueue:
    CAPACITY = 10

    def __init__(self, size = CAPACITY):
        self._data = [None] * DoubleEndedQueue.CAPACITY
        self._front = -1
        self._rear = 0
        self._size = 0
        self.CAPACITY = size

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size <= 0
    
    def is_full(self):
        return self._size == self.CAPACITY

    def addFront(self, e):
        if self.is_full():
            raise OverflowError('Queue is full')

        self._data[self._front % self.CAPACITY] = e
        self._size += 1
        self._front -= 1

    def addRear(self, e):
        if self.is_full():
            raise OverflowError('Queue is full')

        self._data[self._rear % self.CAPACITY] = e
        self._size += 1
        self._rear += 1

    def removeFront(self):
        if self.is_empty():
            raise Empty('Queue is empty')

        temp = self._data[self._front % self.CAPACITY] = None
        self._size -= 1
        self._front += 1

        return temp

    def removeRear(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        temp = self._data[self._rear% self.CAPACITY] = None
        self._size -= 1
        self._rear -= 1

        return temp

    def toString(self):
        return self._data