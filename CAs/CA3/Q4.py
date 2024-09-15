
class Node:
    def __init__(self , val , p , index):
        self.value = val
        self.child = []
        self.p = p
        self.index = index
        self.posht = 0
        self.flag = -1
            


x = input().split()
n = int(x[0])
q = int(x[1])
x = input().split()
nodeList = []
nodeList.append(Node(1  , Node(0 , None , 0) , 1))
for i in range(n-1):
    nodeList.append(Node(i+2 , None , i+2))
for i in range(n-1):
    nodeList[i+1].p = nodeList[int(x[i])-1]
    nodeList[int(x[i])-1].child.append(nodeList[i+1])
res = []
for i in range(q):
    x = list(map(int , input().split()) )
    qnum = x[0]
    x = x[1:]
    cost = 0
    for j in range(qnum):
        nodeList[x[j]-1].p.posht = nodeList[x[j]-1].p.posht + 1
    for j in range(qnum):
        cost = cost + len(nodeList[x[j]-1].child ) + 1 - 2 * nodeList[x[j]-1].posht
    for j in range(qnum):
        nodeList[int(x[j])-1].p.posht = 0
    res.append(cost)
    
    
for x in res:
    print(x)

    