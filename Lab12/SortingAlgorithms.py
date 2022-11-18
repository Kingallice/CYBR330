#Selection Sort
def selection_sort(S):

    for i in range(len(S)):
        min_idx = i

        for j in range(i + 1, len(S)):
            if S[j] < S[min_idx]:
                min_idx = j
        (S[i], S[min_idx]) = (S[min_idx], S[i])
        
#Insertion Sort
def insertion_sort(S):
    """Sort the list using the insertion-sort algorithm."""
    for i in range(1, len(S)):
        key = S[i]

        j = i-1
        while j >= 0 and key < S[j]:
            S[j+1] = S[j]
            j -= 1
        S[j+1] = key

#Quick Sort
def quick_sort(S, a = None, b = None):
    """Sort the list using the quick-sort algorithm."""
    if a == None or b == None:
        a = 0
        b = len(S)-1
    if a >= b: return
    pivot = S[b]
    left = a
    right = b-1
    
    while left <= right:
        while left <= right and S[left] < pivot:
            left += 1
        while left <= right and pivot < S[right]:
            right -= 1
        if left <= right:
            S[left], S[right] = S[right], S[left]
            left, right = left+1, right-1
    
    S[left], S[b] = S[b], S[left]
    quick_sort(S, a, left-1)
    quick_sort(S, left+1, b)

#Heap Sort
def heapify(S, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and S[i] < S[left]:
        largest = left

    if right < n and S[largest] < S[right]:
        largest = right

    if largest != i:
        S[i], S[largest] = S[largest], S[i]
        heapify(S, n, largest)

def heap_sort(S):
    n = len(S)

    for i in range(n // 2 - 1, -1, -1):
        heapify(S, n, i)
    
    for i in range(n - 1, 0, -1):
        S[i], S[0] = S[0], S[i]
        heapify(S, i, 0)

#Merge Sort
def merge(S1, S2, S):
    """Merghe two sorted Python lists S1 and S2 into properly sized list S."""
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i< len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i]
            i += 1
        else:
            S[i+j] = S2[j]
            j += 1
    S

def merge_sort(S):
    """Sort the elements of Python list S using merge-sort algorithm."""
    n = len(S)
    if n < 2:
        return
    
    mid = n//2
    S1 = S[0:mid]
    S2 = S[mid:n]
    merge_sort(S1)
    merge_sort(S2)

    merge(S1, S2, S)