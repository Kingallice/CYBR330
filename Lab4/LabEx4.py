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


def transferStack(S, T):
    T.push(S.pop())
    if len(S) > 0:
        transferStack(S, T)

def emptyStack(S):
    S.pop()
    if len(S) > 0:
        emptyStack(S)

def reverseStack(S):
    T = ArrayStack()
    while S.is_empty() == False:
        T.push(S.pop())
    
    for x in T.toString():
        S.push(x)

x = [1,2,3,4,5,6,7,8,9,10]
y = [7,4,2,4,8]
S = ArrayStack()
T = ArrayStack()

for i in x:
    S.push(i)

for i in y:
    T.push(i)

print('Start:', S.toString(),T.toString())
reverseStack(S)
print('End:', S.toString(),T.toString())
