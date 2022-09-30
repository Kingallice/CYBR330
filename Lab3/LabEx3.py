def minmax(sequence, min = None, max = None):
    current = sequence.pop(0)
    if min == None or min > current:
        min = current
    if max == None or max < current:
        max = current
    if len(sequence) <= 0:
        return [min, max]
    else:
        return minmax(sequence, min, max)

def reverseString(string, reverse = ''):
    reverse += string[-1]
    if len(string) <= 1:
        return reverse
    else:
        return reverseString(string[:-1], reverse)

def evenodd(sequence, evens = [], odds = []):
    current = sequence.pop(0)
    if current % 2 == 0:
        evens += [current]
    else:
        odds += [current]
    if len(sequence) <= 0:
        return evens + odds
    else:
        return evenodd(sequence, evens, odds)

print(minmax([0, 3, 5, 31, 4, 12, 82, 24, -13, -7, 7, 3]))

print(reverseString('pots&pans'))

print(evenodd([1, 3, 3, 2, 5, 8, 3, 2, 9, 3, 0, 3, 2, 6, 8]))