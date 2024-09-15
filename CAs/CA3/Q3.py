import heapq
def getDay(e):
    return int(e[0])
x = input().split()
n = int(x[0])
d = int(x[1])
persons = []
for i in range(n):
    x = input().split()
    persons.append([int(z) for z in x])
persons.sort(key=getDay)
# personsAnger = [y[0] for y in persons]
personsAngerHeap = []
maxAnger = 0
for i in range(n):
    maxAnger = maxAnger + persons[i][1]*persons[i][2]
personIndex = 0
for i in range(d):
    if personIndex < n:
        while (persons[personIndex][0] <= i + 1 ):
            heapq.heappush(personsAngerHeap ,(-1* persons[personIndex][2] , persons[personIndex]))
            personIndex = personIndex + 1
            if personIndex >= n:
                break
    if personsAngerHeap:    
        maxAnger = maxAnger + personsAngerHeap[0][0]
        personsAngerHeap[0][1][1] = personsAngerHeap[0][1][1] -1
        if personsAngerHeap[0][1][1] == 0:
            heapq.heappop(personsAngerHeap)
print(maxAnger)
    
    