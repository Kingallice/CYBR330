#Lab Exercise 1
#Noah Mosel

#A
def is_multiple(n, m):
    if m % n == 0:
        return True
    return False

#B
def minmax(data):
    low = None
    high = None
    for x in data:
        if high == None or x > high:
            high = x
        if low == None or x < low:
            low = x
    return [low, high]

#C
def squares_sum(n):
    total = 0
    for x in range(1, n):
        total += (x*x)
    return total

#D
def count_vowels(string):
    vowels = 0
    for x in string:
        if x in 'aeiou':
            vowels += 1
    return vowels

#E
def remove_punctuation(string):
    out = ''
    for x in string:
        if x.lower() in 'abcdefghijklmnopqrstuvwxyz0123456789 ':
            out += x
    return out
