from random import randint
from Heaps import HeapPriorityQueue

max = 1000      # Top constraint for random integers
n = 100         # Number of random integers to place into list

list = [randint(0, max) for x in range(n)]

heap = HeapPriorityQueue()

for x in list:
    heap.add(x, x)

for x in heap._data:
    print(x._value)
while heap.is_empty() != True:
    print(heap.remove_min())

def getLargest(h, n):
    pass
