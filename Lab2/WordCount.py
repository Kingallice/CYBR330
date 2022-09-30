userInput = input('Enter a list of words to count.')

wordDict = {}
for x in userInput.split(' '):
    x = x.lower()
    if x in wordDict.keys():
        wordDict[x] += 1
    else:
        wordDict[x] = 1

print(wordDict)