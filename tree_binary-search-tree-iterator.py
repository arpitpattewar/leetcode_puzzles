'''
Created on Nov 30, 2018

@author: aavinash

link: https://leetcode.com/problems/binary-search-tree-iterator/
'''

# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.head=root
        self.stack = [root]

        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.head : 
            #print "yes"
            return self.next()
        
        

    def next(self):
        """
        :rtype: int
        """

        tmp=None
        while self.stack:
            #print self.head.val
            #self.stack.append(self.head)
            if self.head.left : 
                self.stack.append(self.head.left)
                self.head = self.head.left
            else:
                tmp = self.stack.pop()
                if self.head.right :
                    self.stack.append(self.head.right)
                    self.head = self.head.right                    
                break
        print tmp.val
        return tmp 
    
    
    def iterative_inorder_traversal(self):
        """
        :rtype: int
        """
        rstask=[]
        lstack=[self.head]

        while lstack:
            #print self.head.val
            #self.stack.append(self.head)
            print [ i.val for i in lstack]
            if self.head.left : 
                lstack.append(self.head.left)
                self.head = self.head.left
            else:
                print self.head.val
                lstack.pop()
                tmp = lstack.pop()
                if tmp:
                    print tmp.val
                    if tmp.right :
                        lstack.append(tmp.right)
                        self.head = tmp
                     
 
#                 if self.head.right :
#                         self.stack.append(self.head.right)
#                         self.head = self.head.right
#                 else:
#                     self.head = self.stack.pop()
#                     if not self.stack : print self.head.val
 
        



if __name__ == '__main__':
    #obj = BSTIterator(TreeNode(1))
    # Your BSTIterator will be called like this:
    a=TreeNode(12)
    b=TreeNode(4)
    c=TreeNode(15)
    d=TreeNode(14)
    e=TreeNode(65)
    f=TreeNode(2)
    
    
    a.left = b
    a.right = c
    c.right = e
    b.left = f
    
    
    
    
    i, v = BSTIterator(a), []
    
    i.iterative_inorder_traversal()
    
    #print i.next().val
    #print i.next().val
#     while i.hasNext(): 
#         v.append(i.next()) 
#         print [i.val for i in v]    

    