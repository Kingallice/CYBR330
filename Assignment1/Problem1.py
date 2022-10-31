from random import randint
import time

n = 100000

S = [randint(0, 4*n) for x in range(n)]
 
def getMode(s):
    """Returns the Mode of the passed sequence s"""
    dict = {}
    for x in s:
        if x in dict.keys():
            dict[x] += 1
        else:
            dict[x] = 1
    mode = None
    for x in dict:
        if mode == None or mode[1] < dict[x]:
            mode = (x, dict[x])
    return mode

timer = time.time()
print("The number that occurs the most is", getMode(S), "\n\tThis took", (time.time() - timer)*1000, "milliseconds.")