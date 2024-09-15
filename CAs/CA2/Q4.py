
NOTFOUND = -1

inp = input().split(' ')
size = int(inp[0])
tests = int(inp[1])
inp = input().split(' ')
positions = dict()
for i in range(size):
    inp[i] = int(inp[i])
for i in range(size):
    positions[i] = inp[i]
inp2 = []
for i in range(tests):
    temp = input().split()
    temp = list(map(int,temp))
    temp.append(i)
    inp2.append(temp)
    
stack = []
top = NOTFOUND
leftX = []
for i in range(0 , size):
    if top == NOTFOUND:
        leftX.append(NOTFOUND)
        if i == size -1:
            break
        else:
            if inp[i] < inp[i+1]:
                stack.append((inp[i] , i))
                top = top + 1            
    else:
        while(top != NOTFOUND):
            if stack[top][0] < inp[i]:
                leftX.append(stack[top][1])
                if i != size - 1:
                    if inp[i] < inp[i+1]:
                        stack.append((inp[i] , i))
                        top = top + 1    
                break
            else:
                stack.pop()
                top = top - 1
        if top == NOTFOUND:
            leftX.append(NOTFOUND)
            if i != size - 1:
                    if inp[i] < inp[i+1]:
                        stack.append((inp[i] , i))
                        top = top + 1 

stack = []
top = NOTFOUND
rightX = []
for i in range(size-1 , -1 , - 1):
    if top == NOTFOUND:
        rightX.append(size)
        if i == 0:
            break
        else:
            if inp[i-1] > inp[i]:
                stack.append((inp[i] , i))
                top = top + 1            
    else:
        while(top != NOTFOUND):
            if stack[top][0] < inp[i]:
                rightX.append(stack[top][1])
                if i != 0:
                    if inp[i-1] > inp[i]:
                        stack.append((inp[i] , i))
                        top = top + 1    
                break
            else:
                stack.pop()
                top = top - 1
        if top == NOTFOUND:
            rightX.append(size)
            if i != 0:
                    if inp[i-1] > inp[i]:
                        stack.append((inp[i] , i))
                        top = top + 1
rightX = rightX[::-1]
lenOfEveryBox = [(rightX[x]-leftX[x]-1) for x in range(0 , size)]
lenOfEveryBox2 = [(inp[x] , x) for x in range(0 , size)]
lenOfEveryBox2.sort()
maxHieght = -1
maxLenOfEveryBox = []
for i in range(size-1 , -1 , -1):
    maxHieght = max(lenOfEveryBox[lenOfEveryBox2[i][1]] , maxHieght)
    maxLenOfEveryBox.append(maxHieght)
maxLenOfEveryBox = maxLenOfEveryBox[::-1]
finalResult = [(lenOfEveryBox2[x][0] , maxLenOfEveryBox[x]) for x in range(size)]
inp2 = sorted(inp2)
ans = [0] * len(inp2)
x = 0
for i in range(len(inp2)):
    while x != len(finalResult) and finalResult[x][0] <= inp2[i][0]:
        x += 1
    if x == 0 and inp2[i][1] > len(inp):
        ans[inp2[i][2]] = 1
    elif ((x == len(finalResult) or inp2[i][1] > finalResult[x][1]) and inp2[i][1] > 0):
        ans[inp2[i][2]] = 1
            
        
for i in range(len(ans)):
    print(ans[i])