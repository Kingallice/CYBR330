from PositionalList import PositionalList

list = [1, 2, 3, 4, 9, 6, 7, 8, 9, 0]
tlist = ['a', 'b', 'c']

pList = PositionalList()

for x in list:
    pList.add_last(x)
#    print(pList.first().element())

#A
def pListMax(list):
    return max(list)

print("Max Element:", pListMax(pList))

print("\nPosition of 4:", pList.find(4)[1],
"\nPosition of 'Hello':", pList.find("Hello")[1])


print("\nOriginal:",[x for x in pList],"\nReversed:", [x for x in reversed(pList)])
#    print(x)

print([x*x for x in range(100)])