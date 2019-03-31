'''
Created on Mar 11, 2019

@author: aavinash
link:  https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

'''



# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root, parent=None):
        """
        Done with stack
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """ 
        stack = [root]
        head = None
        #root = None
        c=-1
        while stack:
            c+=1
            print [ i.val for i in stack ]
            head = stack.pop()

            #print head.val
            if head.right:
                 stack.append(head.right)
            if head.left:
                stack.append(head.left)
                
            if c>0:    
                root.right = head
                root.left = None
                root = root.right                
                                        
            
         

if __name__ == '__main__':
    obj = Solution()
    
    a1 = TreeNode(1)
    a1_lt = TreeNode(2)
    a1_rt = TreeNode(5)
    
    a1.right = a1_rt
    a1.left =a1_lt  
    
    
    c = TreeNode(3)
    d = TreeNode(4)
    
    e = TreeNode(6)
    f= TreeNode(7)
    
    g=TreeNode(71)
    
    a1.left.left = c
    a1.left.right = d
    
    a1.right.left=e
    
    #a1.right.right = f
    
    #a1.right.right.left = g


    
    head=a1
    
    #obj.flatten_3(a1)
    obj.flatten(head)
    

    while head:
        if head.right:
            print head.val
            head= head.right
        else:
            print head.val
            break    
        