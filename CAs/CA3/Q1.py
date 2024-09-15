import sys
import re


INVALID_INDEX = 'invalid index'
OUT_OF_RANGE_INDEX = 'out of range index'
EMPTY = 'empty'


class MinHeap:
    class Node:
        def __init__(self,val):
            self.value = val

    def __init__(self):
        self.heap = []

    def bubble_up(self, index):
        newElement = index
        if type(index) != int:
            raise Exception(INVALID_INDEX)
        if index < 0 or index >= len(self.heap) :
            raise Exception(OUT_OF_RANGE_INDEX)
        if not self.heap:
            raise Exception('empty')
        while True:
            if newElement <= 0:
                break
            if self.heap[newElement] >= self.heap[(newElement-1)//2] or (newElement-1)//2 < 0:
                break
            else : 
                self.heap[newElement] , self.heap[(newElement-1)//2] = self.heap[(newElement-1)//2] , self.heap[newElement]
            newElement = (newElement-1)//2
        

    def bubble_down(self, index):
        newElement = index
        if type(index) != int:
            raise Exception(INVALID_INDEX)
        if index < 0 or index >= len(self.heap) :
            raise Exception(OUT_OF_RANGE_INDEX)
        if not self.heap:
            raise Exception('empty')
        while True:
            if 2*newElement < len(self.heap):
                break
            if self.heap[newElement] > self.heap[2*newElement+1] and self.heap[newElement] <= self.heap[2*newElement+2]:
                self.heap[newElement] , self.heap[2*newElement+1] = self.heap[2*newElement+1] , self.heap[newElement]
                newElement = 2*newElement + 1
            elif self.heap[newElement] > self.heap[2*newElement+2] and self.heap[newElement] < self.heap[2*newElement+1]:
                self.heap[newElement] , self.heap[2*newElement+2] = self.heap[2*newElement+2] , self.heap[newElement]
                newElement = 2*newElement + 2
            else : 
                break

    def heap_push(self, value):
        if not(self.heap):
            self.heap.append(value)
            return
        self.heap.append(value)
        self.bubble_up(len(self.heap)-1)

    def heap_pop(self):
        if not self.heap:
            raise Exception(EMPTY)
        n = len(self.heap)
        x = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        index = 0
        while(True):
            n = len(self.heap)
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            smallest = index
            if left_child < n :
                if self.heap[left_child] < self.heap[smallest]:
                    smallest = left_child
            if right_child < n :
                if self.heap[right_child] < self.heap[smallest]:
                    smallest = right_child
            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break
        return x

    def find_min_child(self, index):
        if type(index) != int:
            raise Exception(INVALID_INDEX)
        if index < 0 or index >= len(self.heap) :
            raise Exception(OUT_OF_RANGE_INDEX)
        left = 2 *index + 1
        right = 2 *index + 2
        n = len(self.heap)
        if left >= n and right < n:
            return right
        if right >= n and left < n:
            return left
        if right >= n and left >= n:
            raise Exception(OUT_OF_RANGE_INDEX)
            return
        if self.heap[left] < self.heap[right]:
            return left
        else:
            return right
        
    def minHeapify(self , index):
        if type(index) != int:
            raise Exception(INVALID_INDEX)
        if index < 0 or index >= len(self.heap) :
            raise Exception(OUT_OF_RANGE_INDEX)
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        n = len(self.heap)
        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left
    
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right
    
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.minHeapify(smallest)
            
    def heapify(self, *args):
        for item in args:
            self.heap_push(item)
        
def getNodeCount(e):
    return e.getCount()
def getCount(e):
    return e[1]
class HuffmanTree:
    class Node:
        def __init__(self , char , count = 0 , left = None , right = None , code = ''):
            self.char = char
            self.count = count
            self.code = code
            self.right = right
            self.left = left
        def setCount(self , count):
            self.count = count
        def getCount(self):
            return self.count
        
    def __init__(self):
        self.head = None
        self.train = []
        self.encode ={}

    def set_letters(self, *args):
        encodingLetters = dict()
        for item in args:
            encodingLetters[item] = ''
            self.train.append([item , 0])
        self.encode = encodingLetters

    def set_repetitions(self, *args):
        for i in range(len(args)):
            self.train[i][1] = args[i]

    def findEveryNodeCode(self , code , node):
        codeNode = code + node.code
        if (not node.left)  and (not node.right):
            self.encode[node.char] = codeNode
        if node.right:
            self.findEveryNodeCode(codeNode,node.right)   
        if node.left:
            self.findEveryNodeCode(codeNode,node.left)
          
               
    def build_huffman_tree(self):
        self.train.sort(key=getCount)
        index = 0
        temp = []
        for i in range(len(self.train)):
            temp.append(self.Node(self.train[i][0] , self.train[i][1]))
        parent = None
        while True :
            if len(temp) <= 1:
                break
            temp.sort(key=getNodeCount)
            rightChild = temp[1]
            leftChild = temp[0]
            parent = self.Node("" , leftChild.count + rightChild.count , leftChild , rightChild , "")
            temp.pop(0)
            temp.pop(0)
            temp.append(parent)
            leftChild.code = leftChild.code + '0'
            rightChild.code = rightChild.code + '1'
        self.head = parent
        self.findEveryNodeCode('' , self.head)
    def get_huffman_code_cost(self):
        cost = 0
        for i in range(len(self.train)):
            cost = cost + self.train[i][1] * len(self.encode.get(self.train[i][0] , ''))
        return cost
    def text_encoding(self, text):
        newEncode = dict()
        newTrain = []
        for i in range(len(text)):
            newEncode[text[i]] = newEncode.get(text[i] , 0) + 1
        for item in newEncode:
            newTrain.append([item , newEncode[item]])
        self.encode = newEncode 
        self.train = newTrain
        self.build_huffman_tree()

class Bst:
    class Node:
        def __init__(self , val):
            self.value = val
            self.right = None
            self.left = None
        pass

    def __init__(self):
        self.head = None

    def insert(self, key):
        if self.head == None:
            self.head = self.Node(key)
            return
        temp = self.head
        found = True
        while (found):
            if temp.value <= key:
                if temp.right:
                    temp = temp.right
                else:
                    temp.right = self.Node(key)
                    found = False
            else:
                if temp.left:
                    temp = temp.left
                else:
                    temp.left = self.Node(key)
                    found = False
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

class Runner:
    dsMap = {'min_heap': MinHeap, 'bst': Bst, 'huffman_tree': HuffmanTree}
    callRegex = re.compile(r'^(\w+)\.(\w+)\(([\w, \-"\']*)\)$')

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

        args = [x.strip() for x in argsList.split(',')] if argsList != '' else []
        args = [x[1:-1] if x[0] in ('"', "'") else int(x) for x in args]

        method = getattr(self.items[itemName], funcName)
        try:
            result = method(*args)
        except Exception as ex:
            print(ex)
        else:
            if result is not None:
                print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
