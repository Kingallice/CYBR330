class SinglyLinkedList:

    class Node:
        def __init__(self, e = None, n = None):
            self._element = e
            self._next = n
        
        def getElement(self):
            return self._element

        def getNext(self):
            return self._next

        def setElement(self, e):
            self._element = e

        def setNext(self, n):
            self._next = n
    
    def __init__(self):
        self._head = None

    def getHead(self):
        return self._head
    
    def addNode(self, e):
        if self._head == None:
            self._head = self.Node(e)
        else:
            curr = self._head
            while curr.getNext() != None:
                curr = curr.getNext()
            else:
                curr.setNext(self.Node(e))
    
    def pop(self):
        answer = None
        if self._head != None:
            curr = self._head
            temp = None
            while curr.getNext() != None:
                temp = curr
                curr = curr.getNext()
            else:
                answer = curr.getElement()
                temp.setNext(None)
        return answer

    def printList(self):
        curr = self._head
        out = []
        while curr.getNext() != None:
            out += [str(curr.getElement())]
            curr = curr.getNext()
        else:
            out += [str(curr.getElement())]
        print("["+(", ".join(out))+"]")

