from random import randint
import time
from SortingAlgorithms import selection_sort, insertion_sort, quick_sort, heap_sort, merge_sort

num = 1000 #Number of random numbers
low = 10 #Min range of randoms
high = 1000 #Max range of randoms

list = [randint(low, high) for x in range(num)]

x = list.copy()
start = time.time()
print("No Sort:\n",x[:10],"\tTime Taken:", (time.time() - start) * 1000, "ms")

x = list.copy()
start = time.time()
selection_sort(x)
print("\nSelection Sort:\n",x[:10],"\tTime Taken:", (time.time() - start) * 1000, "ms")

x = list.copy()
start = time.time()
insertion_sort(x)
print("\nInsertion Sort:\n",x[:10],"\tTime Taken:", (time.time() - start) * 1000, "ms")

x = list.copy()
start = time.time()
quick_sort(x)
print("\nQuick Sort:\n",x[:10],"\tTime Taken:", (time.time() - start) * 1000, "ms")

x = list.copy()
start = time.time()
heap_sort(x)
print("\nHeap Sort:\n",x[:10],"\tTime Taken:", (time.time() - start) * 1000, "ms")

x = list.copy()
start = time.time()
merge_sort(x)
print("\nMerge Sort:\n",x[:10],"\tTime Taken:", (time.time() - start) * 1000, "ms")