'''
Created on Oct 25, 2018

@author: aavinash
link: https://leetcode.com/problems/diameter-of-binary-tree/

'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        pass
    
    
    def getAllLeaves(self, root):
        if root.left: self.getAllLeaves(root.left)
        if root.right: self.getAllLeaves(root.right)
        print root.val
        
        
        

if __name__ == '__main__':
    a1 = TreeNode(1)
    a1_lt = TreeNode(2)
    a1_rt = TreeNode(3)
    
    a1.right = a1_rt
    a1.left =a1_lt  
    
    c = TreeNode(4)
    d = TreeNode(5)
     
    e = TreeNode(6)
    f= TreeNode(7)
     
    a1.left.left = c
    a1.left.right = d
    
    a1.right.left=e
     
    a1.right.right  = f
    
    
    
    obj = Solution()
    obj.getAllLeaves(a1)
