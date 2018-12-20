'''
Created on Dec 17, 2018

@author: aavinash

link::   https://leetcode.com/problems/binary-tree-inorder-traversal/description/
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        

class Solution(object):
    def inorderPredesessor(self, root, p ):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        root = self.root
        
        while root:
            if p.data <= root.data:
                root = root.left
            else:
                pred = root
                root = root.right
                
                
                    
                
                
                
if __name__ == '__main__':
    obj = Solution() 
    
    b=TreeNode(5)
    c=TreeNode(11)
    a=TreeNode(10)
    g=TreeNode(19)
    f=TreeNode(1)
    d=TreeNode(13)
    #a.left  =b
    a.right = c
    a.right.right=g
    print obj.inorderTraversal(a) 
    print obj.kthSmalest(a,2)              
            
            
            