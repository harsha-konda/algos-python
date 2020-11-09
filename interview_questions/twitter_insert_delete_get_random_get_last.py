def addNumbers(a,b):
    sum = a + b
    return sum

num1 = int(input())
num2 = int(input())

print("The sum is", addNumbers(num1, num2))


# Design a data structure with the following operations: add, remove, contains, getLast and getRandom

# { k : Node}
# Node: prev,next

# add O(1)
#  new node 
#  tail of the linked list
# k : Node

# remove O(1)
# check if node is in  hasmap
# if it exists : do delete from the linked list

# contains O(1)
# check if node is in hashmap

#getLast  O(1)
# return tail of the linkedlist

# getRandom O(N)
# N 
# rand()*N = (0,N)
# traverse the linked list 


# key 
# value (i,Node)


# {a : (0,Node),b: (1,Node)}
# [a ,b]
# a -> b




from random import random

class Node:
    def __init__(self,val=None,prevNode=None,nextNode=None,):
        self.val = val    
        self.nextNode = nextNode
        self.prevNode = prevNode        
        
class Store:
    def __init__(self):
        self.keys = {}
        self.order = []
        self.head = Node()
        self.tail = self.head
        
    def remove(self,key):
        if key in self.keys:
            i,node = self.keys[key]
            self.order[-1],self.order[i] = self.order[i],self.order[-1]
            
            lastKey= self.order[i]
            self.keys[lastKey] = i
            self.order.pop()
            
            del self.keys[key]
            
            prevNode = node.prevNode
            if node == self.tail:
                prevNode.nextNode, self.tail = None,prevNode
                node.prevNode = None
                node.nextNode = None

            else:
                nextNode = node.nextNode
                prevNode.nextNode = nextNode
                nextNode.prevNode = prevNode
                node.prevNode,node.nextNode = None,None
                
    def add(self,key):
        if key not in self.keys:
            self.order.append(key)
            
            node = Node(key,self.tail)
            
            self.keys[key] = (len(self.order)-1,node)
            if self.head == self.tail:
                self.head.nextNode = node
                self.tail = node
            else:
                self.tail.nextNode = node
                self.tail = node
        
            
    def contains(self,key):
        if key in self.keys:
            return True
        return False
    
    def getLast(self):
        if len(self.keys) >0:
            return self.tail   
    
    def getRandom(self):
        i = int(random()*len(self.order))
        return self.order[i]
    
        
        
        
        