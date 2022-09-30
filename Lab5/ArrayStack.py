from queue import Empty

class ArrayStack:
    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)
    
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]
    
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

    def toString(self):
        out = []
        for x in self._data.copy():
            out.append(x)
        return out