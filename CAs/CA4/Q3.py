WHITE = 'WHITE'
BLACK = 'BLACK'
GRAY = 'GRAY'
time = 0
result = []
chapy = []
all = []
class Node:
    def __init__(self , val):
        self.value = val
        self.adjences = []
        self.color = WHITE
        self.P = []
        self.start = 0
        self.finish = 0
        self.team = -1
        
def DFS(graph):
    for item in graph:
        item.color = WHITE
        item.p = []
    global time
    time = 0
    for item in graph:
        if item.color == WHITE:
            item.team = True
            DFSVisit(graph , item)
    
            

def DFSVisit(graph , u):
    global time 
    time = time + 1
    u.start = time 
    u.color = GRAY
    # if len(u.adjences) != 1:
    #     chapy.append(u)
    for item in u.adjences[::-1]:
        chapy.append(u)
        if graph[item-1].color == WHITE:
            graph[item-1].p = list(u.p)
            graph[item-1].p.append(u)
            graph[item-1].team = not u.team
            DFSVisit(graph , graph[item-1])
    if len(u.adjences) == 1:
        result.append(u)
    #     chapy.append(u)
    # if len(u.adjences) != 1:
    #     chapy.append(u)
    u.color = BLACK
    time = time + 1
    u.finish = time
    
nodes = []
n  = int(input())
for i in range(n):
    nodes.append(Node(i+1))
for i in range(n-1):
    x = input().split()
    nodes[int(x[0])-1].adjences.append(int(x[1]))
    nodes[int(x[1])-1].adjences.append(int(x[0]))
x = [int(z) for z in input().split()]
DFS(nodes)
for item in range(len(x)-1):
    cur = nodes[x[item]-1].p
    nex = nodes[x[item+1]-1].p
    i = 0
    j = 0
    while cur[i] == nex[j]:
        i = i + 1
        j = j + 1
        if i >= len(cur) or j >= len(nex) :
            break
    all = all + [nodes[x[item]-1].value]
    all = all + [cur[k].value for k in range(len(cur)-1 , i-1 , -1)]
    all.append(cur[i-1].value)
    all = all + [nex[k].value for k in range(j , len(nex))]

all = [item.value for item in nodes[x[0]-1].p] + all  
all = all + [x[-1]] + [item.value for item in nodes[x[-1]-1].p[::-1]][:-1]
if len(all)  > 2*n-2:
    print(-1)
    exit(0)
print(' '.join([str(item) for item in all]))

# if len(result)+1 > 2*n-2:
#     print(-1)
#     exit(0)
# if x == ' '.join([str(item.value) for item in result]) or x == ' '.join([str(item.value) for item in result[::-1]]):
#     print(' '.join([str(item.value) for item in chapy]))
# else :
#     print(-1)