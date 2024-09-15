WHITE = 'WHITE'
BLACK = 'BLACK'
GRAY = 'GRAY'
time = 0

class Node:
    def __init__(self , val):
        self.value = val
        self.enemies = []
        self.color = WHITE
        self.P = None
        self.start = 0
        self.finish = 0
        self.team = -1
        
def DFS(graph):
    for item in graph:
        item.color = WHITE
        item.p = None
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
    for item in u.enemies:
        if graph[item-1].color == WHITE:
            graph[item-1].p = u
            graph[item-1].team = not u.team
            DFSVisit(graph , graph[item-1])
    u.color = BLACK
    time = time + 1
    u.finish = time
    
nodes = []
n , m = [int(x) for x in input().split()]
for i in range(n):
    nodes.append(Node(i+1))
for i in range(m):
    x = input().split()
    nodes[int(x[0])-1].enemies.append(int(x[1]))
    nodes[int(x[1])-1].enemies.append(int(x[0]))
DFS(nodes)
team1 = []
for item in nodes:
    if item.team == -1:
        print(-1)
        exit(0)
    if item.team :
        team1.append(item)
print(len(team1))
print(' '.join([str(item.value) for item in team1]))
