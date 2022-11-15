from random import randint
import time
from SortingAlgorithms import selection_sort, insertion_sort, quick_sort, heap_sort, merge_sort

num = 100000 #Number of random numbers
low = 10 #Min range of randoms
high = 1000 #Max range of randoms

list = [randint(low, high) for x in range(num)]

for i in range(6):
    x = list.copy()
    if i == 0:
        start = time.time()
        print("No Sort:\n\tTime Taken:", time.time() - start)
    if i == 1:
        start = time.time()
        selection_sort(x)
        print("\nSelection Sort:\n\tTime Taken:", time.time() - start)
    if i == 2:
        start = time.time()
        insertion_sort(x)
        print("\nInsertion Sort:\n\tTime Taken:", time.time() - start)
    if i == 3:
        start = time.time()
        quick_sort(x)
        print("\nQuick Sort:\n\tTime Taken:", time.time() - start)
    if i == 4:
        start = time.time()
        heap_sort(x)
        print("\nHeap Sort:\n\tTime Taken:", time.time() - start)
    if i == 5:
        start = time.time()
        merge_sort(x)
        print("\nMerge Sort:\n\tTime Taken:", time.time() - start)