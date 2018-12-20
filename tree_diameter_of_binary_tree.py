'''
Created on Oct 27, 2018

@author: aavinash

link: https://leetcode.com/problems/diameter-of-binary-tree/

Diameter : Number of nodes on the longest path of the binary tree

'''

from LeetCodeTree import TreeNode


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        hl = self.height(root.left)
        hr = self.height(root.right)
        dl = self.diameterOfBinaryTree(root.left)
        dr=  self.diameterOfBinaryTree(root.right)
        
        return max( hl+hr, max(dl,dr))
    
#  
#     def depthAndDiam(self, root):
#         if not root:
#             return 0,0
#         dpl,dil=self.depthAndDiam(root.left)
#         dpr,dir=self.depthAndDiam(root.right)
#         dp=1+max(dpl,dpr)
#         di=max(dpl+dpr, dil,dir)
#         return dp,di
#      
#     def diameterOfBinaryTree(self, root):
#         _,di=self.depthAndDiam(root)
#         return di   
    
    
    def height(self, head=None ):
        if not head : return 0
        
        
        hl,hr=0,0
        #if not head.left and head.right : return -1
        if head.left : hl = hl+self.height(head.left)
        if head.right : hr = hr+self.height(head.right)
        return 1+max(hl,hr)
    
        
        
        
        

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
    
    
    a1.left.left.left = e
    a1.left.left.right = f
    
    
    g=TreeNode(8)
    h=TreeNode(9)
    i=TreeNode(8)
    j=TreeNode(9)
    
    a1.left.left.left.left=g
    a1.left.left.left.right=h
          
#     a1.right.left.left = j
#     a1.right.left.right = i 
     
    obj = Solution()
    
    print obj.diameterOfBinaryTree(a1)
    print obj.height(a1)
    print obj.height(a1.left)

    
    