'''
Created on Dec 19, 2018

@author: aavinash


link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/    
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root :
            stack1_l_r=[root]
            stack2_r_l=[]
            final_result=[]
            while stack1_l_r or stack2_r_l:
                result=[]
                while stack1_l_r:
                    current = stack1_l_r.pop()
                    result.append(current.val)
                    #Adding left child first
                    if current.left : stack2_r_l.append(current.left)
                    if current.right : stack2_r_l.append(current.right)
                if result : final_result.append(result)     
                    
                result=[]    
                while stack2_r_l :
                    current = stack2_r_l.pop()
                    result.append(current.val)
                    #Adding right child first
                    if current.right : stack1_l_r.append(current.right)
                    if current.left : stack1_l_r.append(current.left) 
                if result : final_result.append(result)  
            return final_result  
        else: return []      
              
                
                
    
    
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
    
    #a1.left.left = c
    #a1.left.right = d
    
    a1.right.left=e  
    a1.right.right=f
    
    #a1.left.left.right= TreeNode(12)
    
    
    
    
    obj = Solution()
    
    print obj.zigzagLevelOrder(a1)
                                      
                
                
                
        