from itertools import permutations
from collections import deque
rootGraph = "abcdefgh"
    
n = int(input())
rootGraph = rootGraph[0:n]
dictElements = permutations(rootGraph[0:n])
myDict = dict()
for item in list(dictElements) : myDict[''.join(item)] = -1
mySaf = deque()
level = 0
mySaf.append(rootGraph)
mySaf.append(level)
while mySaf:
    element = mySaf.popleft()
    if type(element) == str:
        if myDict[element] != -1:
            pass
        else :
            myDict[element] = level
            for k in range(n) : 
                for z in range(k+1 , n) : mySaf.append(element[0:k]+element[k:z+1][::-1]+element[z+1:]) 
    else :
        if mySaf:
            mySaf.append(element+1)
            level = level + 1
        else:
            break
q = int(input())
result = []
keys = dict()
for i in range(q):
    x = input().split()
    res = ""
    for j in range(n):
        keys[x[1][j]] = rootGraph[j]
    for j in range(n):
        res = res + keys[x[0][j]]
    # print(myDict[res])
    result.append(myDict[res])
print('\n'.join([str(x) for x in result]))