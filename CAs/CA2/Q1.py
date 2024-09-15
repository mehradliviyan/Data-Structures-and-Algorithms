import sys
import re


class Queue():
    def __init__(self, *args):
        self.front = 0
        self.rear = 0
        self.q = []
    def getSize(self):
        return self.rear - self.front 
    def enqueue(self , value):
        self.q.append(value)
        self.rear = self.rear + 1
    def dequeue(self):
        # if self.isEmpty():
        #     return "EMPTY"
        self.front = self.front + 1
        return self.q[self.front-1]
    def isEmpty(self):
        return self.front == self.rear
    def getInOneLine(self):
        # if self.isEmpty():
        #     return 'EMPTY'
        return(' '.join(self.q[self.front : self.rear]))
            
class Stack():
    def __init__(self , size = 10):
        self.top = -1
        self.s = []
        self.size = size
    def isEmpty(self):
        return True if self.top == -1 else False
    def push(self , value):
        # if self.top + 1 == self.size:
        #     return "FULL"
        self.s.append(value)
        self.top = self.top + 1
    def pop(self):
        # if self.isEmpty():
        #     return 'EMPTY'
        self.top = self.top -1
        return self.s[self.top + 1]
    def put(self , value):
        # if self.isEmpty():
        #     return 'EMPTY'
        topValue = self.s[self.top]
        self.s[self.top] = value
        # return topValue
    def peek(self):
        return self.s[self.top]
    def expand(self):
        self.size = self.size * 2
    def getInOneLine(self):
    #     if self.isEmpty():
    #         return 'EMPTY'
        return(' '.join(self.s[0 : self.top+1]))
    def getSize(self):
        return self.top + 1

    def getCapacity(self):
        return self.size


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node(None)

    def getList(self):
        current = self.head.next
        NodeList = []
        while current != None:
            NodeList.append(current.data)
            current = current.next
        return (' '.join(NodeList))
    
    def insertFront(self, new_data):
        temp = self.head.next
        self.head.next = Node(new_data)
        self.head.next.next = temp
        
    def insertEnd(self, new_data):
        temp = self.head.next
        perv = self.head
        while temp != None:
            temp = temp.next
            perv = perv.next
        perv.next = Node(new_data)

    def reverse(self):
        prev = None
        cur = self.head.next
        while(cur != None):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head.next = prev


class Runner:
    dsMap = {'stack': Stack, 'queue': Queue, 'linked_list': LinkedList}
    callRegex = re.compile(r'^(\w+)\.(\w+)\(([\w, ]*)\)$')

    def __init__(self, inputSrc):
        self.input = inputSrc
        self.items = {}

    def run(self):
        for line in self.input:
            line = line.strip()
            action, _, param = line.partition(' ')
            actionMethod = getattr(self, action, None)
            if actionMethod is None:
                return
            actionMethod(param)

    def make(self, params):
        itemType, itemName = params.split()
        self.items[itemName] = self.dsMap[itemType]()

    def call(self, params):
        regexRes = self.callRegex.match(params)
        itemName, funcName, argsList = regexRes.groups()
        args = argsList.split(',') if argsList != '' else []

        method = getattr(self.items[itemName], funcName)
        result = method(*args)
        if result is not None:
            print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
