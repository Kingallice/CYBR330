from random import randint
from PriorityQueue import UnsortedPriorityQueue, SortedPriorityQueue

PQ1 = UnsortedPriorityQueue()
PQ2 = UnsortedPriorityQueue()

for x in [randint(0, 100) for i in range(1000)]:
    PQ1.add(i, x)