# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        def validIndex(*args):
            for arg in args:
                if arg<0 or arg>len(inorder)-1:
                    return False
            return True

        def buildTree(p_s,p_e,i_s,i_e):
            if p_s<0 or p_e < 0 or p_e < p_s or i_s >=len(inorder):
                return None

            node = TreeNode(postorder[p_e])
            i = inorder.index(postorder[p_e])

            left = buildTree(p_s,p_e-(i_e-i+1),i_s,i-1)
            right = buildTree(p_e-(i_e-i),p_e-1,i+1,i_e)

            node.left = left
            node.right = right

            return node

        return buildTree(0,len(inorder)-1,0,len(postorder)-1)


