from tkinter.messagebox import QUESTION
from ArrayStack import ArrayStack
from ArrayQueue import ArrayQueue
from DoubleEndedQueue import DoubleEndedQueue

stack = ArrayStack()

elements = ['Mark', 3, 5, 3, 2, 'ALF']

for x in elements:
    stack.push(x)

def findElement(S, x):
    Q = ArrayQueue()
    found = False

    while S.is_empty() == False:
        temp = S.pop()
        Q.enqueue(temp)
        if temp == x:
            found = True
            break
    tempArr = []
    while Q.is_empty() == False:
        tempArr += [Q.dequeue()]
    while len(tempArr) > 0:
        S.push(tempArr.pop(-1))
    return found

print(stack.toString())
print(findElement(stack, 2))
print(stack.toString())