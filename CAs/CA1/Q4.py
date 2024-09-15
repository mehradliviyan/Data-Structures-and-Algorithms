word = input()
fristNumber = 0
secondNumber = 0
thiredNumber = 0
res = False
for firstNumberIndex in range(1,len(word)):
    fristNumber = word[0:firstNumberIndex]
    for secondNumberIndex in range(firstNumberIndex+1 , len(word)):
        secondNumber = word[firstNumberIndex: secondNumberIndex]
        numberOfPassIndex = secondNumberIndex 
        while True :
            thiredNumber = int(fristNumber) + int(secondNumber)
            if numberOfPassIndex  == len(word):
                res = True
            
            if len(str(thiredNumber)) + numberOfPassIndex > len(word):
                break
            
            if thiredNumber == int(word[numberOfPassIndex : numberOfPassIndex+len(str(thiredNumber))]) and fristNumber[0] != '0' and secondNumber[0] != '0' :
                numberOfPassIndex = numberOfPassIndex + len(str(thiredNumber))
                fristNumber = secondNumber
                secondNumber = str(thiredNumber)
                thiredNumber = int(fristNumber) + int(secondNumber)
            else:
                break
            
if res :
    print('YES')
else:
    print('NO')