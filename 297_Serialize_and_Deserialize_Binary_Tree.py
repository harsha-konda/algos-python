# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
import json
class TreeNode(object):
    def __init__(self, x,left=None,right=None):
        self.val = x
        self.left = left
        self.right = right

# do a bfs
# store a complete tree
# time limit exceeded for a case
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        nodes = [root]
        allNone = False
        results = []
        while(not allNone):
            nextNodes = []
            allNone = True
            result = []
            i = 0
            while(i<len(nodes)):
                if nodes[i] is not None:
                    result.append(nodes[i].val)
                    if (nodes[i].left is not None) or (nodes[i].right is not None):
                        allNone = False
                    nextNodes.append(nodes[i].left)
                    nextNodes.append(nodes[i].right)
                else:
                    result.append(None)
                    nextNodes.append(None)
                    nextNodes.append(None)

                i+=1
            results.append(result)
            if not allNone:
                nodes = nextNodes
        return json.dumps(results)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = json.loads(data)
        def constructTree(data,level,index):
            if level == len(data):
                return None
            if data[level][index] is None :
                return None

            left = constructTree(data,level+1,2*index)
            right = constructTree(data,level+1,2*index+1)
            return TreeNode(data[level][index],left,right)
        return constructTree(data,0,0)
# Your Codec object will be instantiated and called as such:
codec = Codec()

# preorder traversal
class Codec:
    def serialize(self, root):
        result = []
        def preorder(node):
            if node:
                result.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
            else:
                result.append("*")
        preorder(root)
        return ",".join(result)

    def deserialize(self,data):
        data = data.split(",")
        dataIterator = iter(data)

        def parseTree():
            val = next(dataIterator)
            if val == '*':
                return
            node = TreeNode(int(val))
            left = parseTree()
            right = parseTree()
            node.left = left
            node.right = right
            return node
        return parseTree()
