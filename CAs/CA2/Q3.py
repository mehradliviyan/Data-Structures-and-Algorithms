
def getInput():
    n = int(input())
    colors = []
    for item in range(n):
        colors.append(int(input()))
    return {
        'n':n,
        'colors' : colors
    }

def remove2SameLetterInRow(colors):
    temp = []
    temp.append(colors[0])
    for i in range(1 , len(colors)):
        if colors[i] != colors[i-1]:
            temp.append(colors[i])
    return temp

def splitByZeros(colors):
    temp = []
    colors2 = []
    for item in colors:
        if item == 0 and len(temp) != 0:
            colors2.append(temp)
            temp = []
        else:
            if item != 0:
                temp.append(item)
                            
    if temp:
        colors2.append(temp)
    return colors2

def detectSameNumBetweenZero(colors):
    temp = set()
    for subList in colors:
        for element in subList:
            if element in temp:
                print(-1)
                exit(0)
        temp.update(subList)
        
def deleteSingleCharAndMakeResult(colors):
    results = [0 for i in colors]
    temp = []
    for h in range(len(colors)):
        temp2 = []
        sub = colors[h]
        count = dict()
        for item in sub:
            count[item] = count.get(item, 0) + 1
        temp2 = [x for x in sub if count[x] > 1]
        if len(temp2) != len(sub):
            results[h] = 1
        temp.append(temp2)            
    return [results , temp]

def findLastAccourns(colors):
    temp = []
    for sub in colors:
        occurs = {}
        for i in range(0 , len(sub)):
            occurs[str(sub[i])] = i
        temp.append(occurs)
    return temp
    
def makeLastResults(colors , results , lastAccourns):
    for h in range(len(colors)):
        stack = []
        maxValue = 0
        top = -1
        sub = colors[h]
        for i in range(len(sub)):
            if top != -1:
                if stack[top] != sub[i]:
                    stack.append(sub[i])
                    top = top + 1
                    maxValue = max(maxValue , top+1)
                else:
                    if lastAccourns[h][str(sub[i])] == i:    
                        stack.pop()
                        top = top - 1
            else:
                stack.append(sub[i])
                top = top + 1
                maxValue = max(maxValue , top+1)
        if top != -1:
            print(-1)
            exit(0)
        else:
            results[h] = results[h] + maxValue
    
            
def main():
    inp = getInput()
    colors = remove2SameLetterInRow(inp['colors'])
    colors = splitByZeros(colors)
    detectSameNumBetweenZero(colors)
    [results,colors] = deleteSingleCharAndMakeResult(colors)
    lastAccourns = findLastAccourns(colors)
    makeLastResults(colors , results , lastAccourns)
    print(max(results))
    
main()