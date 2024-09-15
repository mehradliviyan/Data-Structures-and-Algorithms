allMasks = {}
def createAllMasks(str):
    if len(str) == 10:
        allMasks[str] = 0
        return 
    createAllMasks(str + '0')
    createAllMasks(str + '1')
 
def filliper(char):
    if char == '1':
        return '0'
    else:
        return '1'
    
     
createAllMasks('')
allMasks['0000000000'] = 1

word = input()

bitMask = '0000000000'
sum = 0
for item in word:
    bitMask = bitMask[:ord(item) - ord('a')] + filliper(bitMask[ord(item) - ord('a')]) + bitMask[ord(item) - ord('a') + 1:]
    for i in range(10):
        temp = bitMask[:i] + filliper(bitMask[i]) + bitMask[i+1:]
        #print(temp)
        sum += allMasks[temp]
    # print(bitMask)
    allMasks[bitMask] += 1
    sum = sum + allMasks[bitMask] - 1
    
print(sum)
        