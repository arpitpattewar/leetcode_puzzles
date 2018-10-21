'''
Created on Oct 7, 2018

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
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            result = []
            head = root
            stack = [ root ]
            while stack:
                if head.left :
                    stack.append(head.left) 
                    head = head.left
                else:
                    tmp = stack.pop()  
                    result.append(tmp.val)
                    if tmp.right: 
                        stack.append(tmp.right)
                        head=tmp.right 
            return result 
        else:
            return []  
        
        
    def kthSmalest(self, root,k):
        """
        :type root: TreeNode
        :rtype: List[int]
        link : https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
        """
        if root:

            head = root
            stack = [ root ]
            c=0
            while stack:
                if head.left :
                    stack.append(head.left) 
                    head = head.left
                else:
                    tmp = stack.pop() 
                    c+=1
                    #print tmp.val
                    if c == k : 
                        return  tmp.val
                    if tmp.right: 
                        stack.append(tmp.right)
                        head=tmp.right 
                
                
                
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
            
            
            