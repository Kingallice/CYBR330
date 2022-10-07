from ast import Break
from SinglyLinkedList import SinglyLinkedList
from CircularlyLinkedList import CircularlyLinkedList
from DoublyLinkedList import DoublyLinkedList

def Single_countNodes(node, count = 1):
    curr = node.getNext()
    if curr != None:
        return Single_countNodes(curr, count+1)
    else:
        return count

def Circular_countNodes(list):
    temp = list.head
    count = 0
    if temp == None:
        return count
    while True:
        count += 1
        if temp.next == list.head:
            return count
        temp = temp.next

def Double_middleNode(list):
    temp1 = list.start_node
    temp2 = list.start_node.next
    while temp2 != None:
        temp2 = temp2.next.next
        temp1 = temp1.next
    return temp1.item

x = [1, 2, 3, 4, "Middle", 6, 7, 8, 9]

Slist = SinglyLinkedList()

for i in x.copy():
    Slist.addNode(i)

print("Singly -", Single_countNodes(Slist.getHead()))

Clist = CircularlyLinkedList()

for i in x.copy():
    Clist.add_data(i)

print("Circularly -", Circular_countNodes(Clist))

Dlist = DoublyLinkedList()

for i in x.copy():
    Dlist.InsertToEnd(i)

print(Double_middleNode(Dlist))