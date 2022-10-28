from random import randint
from re import X
import time
from PriorityQueue import UnsortedPriorityQueue, SortedPriorityQueue

PQ1 = UnsortedPriorityQueue()
PQ2 = SortedPriorityQueue()

BASENUM = 1000  #Number of Random Numbers to add
MAXRAND = 1000000   #Largest random int to add

for i in range(BASENUM):
    x = randint(0, MAXRAND)
    PQ1.add(x, x)
    PQ2.add(x, x)

def time_add(pq1, pq2, num):
    """Returns time to add num of entries to each Priority Queue in form (time1, time2) tuple."""
    timer = time.time()
    for i in range(num):
        x = randint(0, MAXRAND)
        pq1.add(x, x)
    Time1 = time.time() - timer

    timer = time.time()
    for i in range(num):
        x = randint(0, MAXRAND)
        pq2.add(x, x)
    Time2 = time.time() - timer
    return (Time1, Time2)

def time_smallest(pq1,pq2, num):
    """Returns time to get the smallest num entries of each Priority Queue in form (time1, time2) tuple."""
    timer = time.time()
    for i in range(num):
        x = pq1.remove_min()
    Time1 = time.time() - timer
    timer = time.time()
    for i in range(num):
        x = pq2.remove_min()
    Time2 = time.time() - timer
    return (Time1, Time2)

print("The times to add 100 random numbers to PQ1 and PQ2 are", time_add(PQ1,PQ2,100))
print("The times to get the smallest 100 numbers in PQ1 and PQ2 are", time_smallest(PQ1,PQ2,100))