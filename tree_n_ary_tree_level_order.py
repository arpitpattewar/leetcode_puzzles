'''
Created on Jan 24, 2019

@author: aavinash
link: https://leetcode.com/problems/n-ary-tree-level-order-traversal/submissions/

'''



"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        stack1=[]
        stack2=[]
        r=[]
        if root : stack1.append(root)
        while stack1:
          s=[]   
          while stack1:
             current = stack1.pop(0)
             s.append(current.val)
             if current.children : 
                for child in current.children:
                    stack2.append(child)
          stack1=stack2
          stack2=[]
          r.append(s)
        return r    
                
                
            