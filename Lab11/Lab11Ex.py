from Maps import UnsortedTableMap, PositionalListUnsortedTableMap
from random import randint

max = 100
num = 10

map = PositionalListUnsortedTableMap()

#Creates a list to use to fill the map
list = [(randint(0, max//2), randint(0, max)) for x in range(num)]

#Fills the map and logs any changes on keys that have values changed
changed = []
for x in list:
    try:
        temp = map[x[0]]
        map[x[0]] = x[1]
        changed.append(str(x[0]) + " - " + str((temp, map[x[0]])))
    except KeyError:
        map[x[0]] = x[1]

#Gets all items in map
items = []
for x in map:
    items += [(x, map[x])]

slen = len(map)

#Gets all keys in map
keys = []
for x in map:
    keys += [x]

#Delete a random key from the map
delLoc = keys.pop(randint(0, len(keys) - 1))
deleted = (delLoc, map[delLoc])
del map[delLoc]

#Gets items in map after delete occurs
afterDel = []
for x in map:
    afterDel.append((x, map[x]))

dlen = len(map)

#Uses pop to remove a random key from the map
popKey = keys.pop(randint(0, len(keys) - 1))
popped = map.pop(popKey)

#Gets all items left in map after pop occurs
afterPop = []
for x in map:
    afterPop.append((x, map[x]))

print("Items:\t\t\t", items, 
    "\nLength:\t\t\t", slen, 
    "\nChanged (OLD,NEW):\t", changed,
    "\n\nDeleted:\t\t", deleted,
    "\nAfter Deletion:\t\t", afterDel,
    "\nLength:\t\t\t", dlen, 
    "\n\nPopped Value at",str(popKey)+":\t", popped,
    "\nAfter Pop:\t\t", afterPop,
    "\nLength:\t\t\t", len(map))