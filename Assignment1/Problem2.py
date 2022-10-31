from random import randint
import time
import matplotlib.pyplot as plt
import numpy as np

def prefix_average1(S):
    """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
    n = len(S)
    A = [0] * n
    for j in range(n):
        total = 0
        for i in range(j+1):
            total += S[i]
        A[j] = total / (j+1)
    return A

def prefix_average2(S):
    """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
    n = len(S)
    A = [0] * n
    for j in range(n):
        A[j] = sum(S[0:j+1]) / (j+1)
    return A

def prefix_average3(S):
    """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
    n = len(S)
    A = [0] * n
    total = 0
    for j in range(n):
        total += S[j]
        A[j] = total / (j+1)
    return A

def compare(n = 16):
    """Will return a dictionary containing 'size':'time' pairs for each average algorithm. 
        The input n determines the largest 2^n size to be used for a input list."""

    dict1 = {}
    dict2 = {}
    dict3 = {}
    for i in range(1,n):
        list = [randint(0, 1000) for x in range(2**i)]

        #Times func1
        timer = time.time()
        prefix_average1(list)
        dict1[i] = (time.time()-timer)
    
        #Times func2
        timer = time.time()
        prefix_average2(list)
        dict2[i] = (time.time()-timer)
    
        #Times func3
        timer = time.time()
        prefix_average3(list)
        dict3[i] = (time.time()-timer)
    
    return (dict1, dict2, dict3)

plt.title('Time Comparisons for Average Functions')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
func = 1
for x in compare():
    plt.loglog(x.keys(), x.values(), label=("prefix_average" + str(func)))
    func +=1

plt.legend(loc='upper center')
plt.show()