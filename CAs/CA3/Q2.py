class Bst:
    class Node:
        def __init__(self , val , p , index):
            self.value = val
            self.right = None
            self.left = None
            self.p = p
            self.index = index
        pass

    def __init__(self):
        self.head = None

    def insert(self, key , index):
        if self.head == None:
            self.head = self.Node(key , None , index)
            return self.head
        temp = self.head
        found = True
        tempList = []
        tempList.append(temp)
        while (found):
            if temp.value <= key:
                if temp.right:
                    temp = temp.right
                else:
                    temp.right = self.Node(key , tempList , index)
                    found = False
                    return temp.right
            else:
                if temp.left:
                    temp = temp.left
                else:
                    temp.left = self.Node(key , tempList , index)
                    found = False
                    return temp.left
            tempList.append(temp)
    def inorder(self):
        inorderList = []
        self.makeInorderList(inorderList , self.head)
        return ' '.join(inorderList)
    
    def makeInorderList(self , list , sub):
        if sub == None:
            return
        self.makeInorderList(list , sub.left)
        list.append(str(sub.value))
        self.makeInorderList(list , sub.right)   
    def findBestP(self , a , b):
        aNode = self.head
        bNode = self.head
        temp = self.head
        afound = False
        bfound = False
        while aNode == bNode:
            if aNode.value <= a:
                if aNode.right:
                    aNode = aNode.right
                else:
                    afound = True
            else:
                if aNode.left:
                    aNode = aNode.left
                else:
                    afound = True
            if bNode.value <= a:
                if bNode.right:
                    bNode = bNode.right
                else:
                    bfound = True
            else:
                if bNode.left:
                    bNode = bNode.left
                else:
                    bfound = True
        return aNode.p
                
        
n = int(input())
tree = Bst()
nlist = []
x = input().split()
out1 = []
for i in range(n):
    y = int(x[i])
    nlist.append(y)
    z = tree.insert(y , i)
    out1.append(z)
x = input().split()
a = int(x[0])
b = int(x[1])
out2 = []
for i in range(1 , len(out1)):
    out2.append(str(out1[i].p[-1].value))
print(' '.join(out2))
aNode = out1[a-1]
bNode = out1[b-1]
best = -1
for i in range(min(len(aNode.p) , len(bNode.p))):
    if aNode.p[i] == bNode.p[i]:
        best = bNode.p[i].index
if aNode in bNode.p:
    best = aNode.index
if bNode in aNode.p:
    best = bNode.index
if aNode == bNode:
    best = bNode.index
print(best+1)
