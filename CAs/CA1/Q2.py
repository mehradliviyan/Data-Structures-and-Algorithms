import math
rounds = int(input())
results = []

def judge(myTime , firendTime):
    if firendTime[0:5] <= firendTime[9:14]:
        if myTime[0:5] >= firendTime[0:5] and myTime[0:5] <= firendTime[9:14]:
            return True
        else :
            return False
    else:
        if myTime[0:5] <= firendTime[0:5] and myTime[0:5] >= firendTime[9:14]:
            return True
        else :
            return False

for item in range(0 , rounds):
    myTime = input()
    if  myTime[0:2] == '12':
        myTime = '00' + myTime[2:]
    if myTime[6] == 'P' :
        myTime = str(int(myTime[0:2]) + 12) + myTime[2:]
    numOfFriend = int(input())
    result = ''
    for item in range(0 , numOfFriend):
        firendTime = input()
        if firendTime[0:2] == '12':
            firendTime = '00' + firendTime[2:]
        if firendTime[6] == 'P' :
            firendTime = str(int(firendTime[0:2] ) + 12) + firendTime[2:]
        if firendTime[9:11] == '12':
            firendTime = firendTime[:9] + '00' + firendTime[11:]
        if firendTime[15] == 'P' :
            firendTime = firendTime[:9] + str(int(firendTime[9:11]) + 12) + firendTime[11:]
        if judge(myTime , firendTime):
            result = result + '1'
        else :
            result = result + '0'
    results.append(result)
    
for item in results:
    print(item)