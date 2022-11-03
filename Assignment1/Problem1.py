from random import randint
import time

n = 50000000

timer = time.time()
S = [randint(0, 4*n) for x in range(n)]
print(time.time() - timer)
 
def getMode(s):
    """Returns the Mode of the passed sequence s"""
    dict = {}
    for x in s:
        if x in dict.keys():
            dict[x] += 1
        else:
            dict[x] = 1
    mode = None
    modes = []
    for x in dict:
        if mode == None or mode[1] < dict[x]:
            mode = (x, dict[x])
            modes = [x]
        elif mode[1] == dict[x]:
            modes.append(x)
    return (mode[1], insertionSort(modes))

def insertionSort(s):
    list = [s[0]]
    for x in s[1:]:
        for i in range(len(list)):
            if x >= list[i]:
                list.insert(i,x)
                break
        else:
            list.append(x)
    return list
    
timer = time.time()
k = getMode(S)
print("The numbers that occur the most are", k[1], "which occur", k[0], "times.\n\tThis took", (time.time() - timer)*1000, "milliseconds.")