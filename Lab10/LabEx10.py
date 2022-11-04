from random import randint
from Heaps import HeapPriorityQueue

max = 1000      # Top constraint for random integers
num = 10        # Number of random integers to place into list

list1 = [randint(0, max) for x in range(num)]
list2 = [randint(0, max) for x in range(num)]

heap1 = HeapPriorityQueue()
heap2 = HeapPriorityQueue()

for x in list1:
    heap1.add(x, x)
for x in list2:
    heap2.add(x, x)

def getLargest(h, n):
    list = []
    maxes = [None] * n
    while not h.is_empty():
        item = h.remove_min()
        for i in range(len(maxes)):
            if maxes[i] == None:
                maxes[i] = item[1]
                break
            elif None not in maxes and min(maxes) < item[1]:
                maxes[maxes.index(min(maxes))] = item[1]
                break
        list.append(item)
    for x in list:
        h.add(x[0], x[1])
    maxes.sort()
    return maxes

def mergeHeaps(h1, h2):
    list1, list2 = [], []
    while not h1.is_empty():
        list1.append(h1.remove_min())
    while not h2.is_empty():
        list2.append(h2.remove_min())

    heapOut = HeapPriorityQueue()
    for x in list1:
        h1.add(x[0], x[1])
        heapOut.add(x[0], x[1])
    for x in list2:
        h2.add(x[0], x[1])
        heapOut.add(x[0], x[1])
    return heapOut

print("Heap1:", heap1, "\nHeap2:", heap2)
print("\nThe three largest integers in Heap1 are",getLargest(heap1, 3))
print("\nHeap1:", heap1, "\nHeap2:", heap2)
print("\nThe merged heap resulted from Heap1 and Heap2 is\n",mergeHeaps(heap1, heap2))
print("\nHeap1:", heap1, "\nHeap2:", heap2)