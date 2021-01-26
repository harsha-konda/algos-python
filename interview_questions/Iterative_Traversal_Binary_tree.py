"""

     1
  2     3
 4 5   6 7

4 2 5 1 6 3 7

class Iterator {
    
    bool hasNext()
    
    int next()
}


 
"""
class Node:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

"""
Recursive
"""

# class Iterator:
#     def __init__(self,root):
#         self.order = []
#         self.root = root
#         self.i = 0
#     def traversal(self,node):
#         if not self.node:
#             return
        
#         traversal(self.node.left)
#         self.order.append(node)
#         traversal(self.node.right)
        
#     def hasNext(self):
#         return self.i < len(self.order)

#     def next(self):
#         node = self.order[self.i]
#         self.i+=1
#         return node
        
"""
Iterative
"""
class Iterator:
    def __init__(self,root):
        self.stack = []
        self.currentNode = root
        self.i = 0
                
    def hasNext(self):
        return self.currentNode != None or len(self.stack) > 0

    def next(self):
        if not self.hasNext():
            raise Exception("Reached the end of the tree")
        
        result = None
        if self.currentNode !=None:
            node = self.currentNode
            while(node.left):
                self.stack.append(node)
                node = node.left
            self.stack.append(node)    
            
        if self.stack:
            result = self.stack.pop()
            self.currentNode = result.right
        return result
"""
   1
  2     3
 4 5   6 7

4 2 5 1 6 3 7

"""
ex1 = Node(1,Node(2,Node(4),Node(5)),Node(3,Node(6),Node(7)))
iter = Iterator(ex1)
assert(iter.hasNext() == True)
print(iter.next().value)
assert(iter.hasNext() == True)
print(iter.next().value)
assert(iter.hasNext() == True)
print(iter.next().value)
assert(iter.hasNext() == True)
print(iter.next().value)
assert(iter.hasNext() == True)
print(iter.next().value)
assert(iter.hasNext() == True)
print(iter.next().value)
assert(iter.hasNext() == True)
print(iter.next().value)
assert(iter.hasNext() == False)


print("Tree 2")
ex2 = Node(1,None,Node(3,None,Node(7,None,Node(8))))
iter = Iterator(ex2)
assert(iter.hasNext() == True)
print(iter.next().value)
print(iter.next().value)
print(iter.next().value)
print(iter.next().value)
    
print("Tree 3")
ex3 = None
iter = Iterator(ex3)
assert(iter.hasNext() == False)


print("Tree 4")
ex4 = Node(1,Node(3,Node(7,Node(8))))
iter = Iterator(ex4)
assert(iter.hasNext() == True)
assert(iter.next().value==8)
assert(iter.next().value==7)
assert(iter.next().value==3)
assert(iter.next().value==1)

        
        
        
        
        
