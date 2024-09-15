n = int(input())
numbers = input().split(' ')
possition = dict()
for i in range(n):
    possition[int(numbers[i])] = i + 1

Stack = []
top = -1
perv = dict()
for i in range(n , 0 , -1):
    perv[i] = -1
for item in range(n , 0 , -1):
    while(top != -1):
        topStack = Stack[top]
        if possition[topStack] >= possition[item]:
                Stack.pop()
                top = top - 1
        else:
            perv[possition[item]] = possition[topStack] 
            break
    Stack.append(item)
    top = top + 1
    
Stack = []
top = -1 
answer = 0
print(0)
for i in range(1 , n+1):
    while top != -1:
        if Stack[top] >= possition[i]:
            answer = answer - 1
            Stack.pop()
            top = top - 1
            continue
        break
    if perv[possition[i]] != -1 and top == -1:
        answer = answer + 1
        Stack.append(possition[i])
        top = top + 1
    elif perv[possition[i]] != -1 and perv[possition[i]] != perv[Stack[top]]:
        answer = answer + 1
        Stack.append(possition[i])
        top = top + 1
    print(answer)
        