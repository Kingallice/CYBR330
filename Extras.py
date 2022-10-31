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