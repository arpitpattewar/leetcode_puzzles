'''
Created on Sep 8, 2018

@author: aavinash

link: https://leetcode.com/problems/binary-tree-tilt/description/
'''



# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
         
         
class Tree:
    def __init__(self, tn):
        self.root = tn
    def add_left(self, p, c):
        #print "parent is {}".format(p.val)
        p.left =c 
    def add_right(self, p, c):
        p.right =c   
         
                
         
         
         



class Solution(object):
    
    

        
    
    def display(self, n ):
        print "self node is {}".format(n.val)
        if n.left :  self.display(n.left)
        if n.right :  self.display(n.right)  
        
    def f(self, root):
        print dir(root)
        l = root
        r = root
        tl=tr=0
        while l.left:
            tl+=self.sumallchild(l.left)
            print tl
            if l.left.left: l=l.left
            else: break
            
        while r.right:
            tr+=self.sumallchild(r.right)
            print tr
            if r.right.right : r=r.right
            else: break
            #r=r.right  
            
        return abs(tl+root.left.val - (tr+root.right.val)   )
            
            

                     
    def sumallchild(self, n ):

        s=0

        if n.left : 
            s=s+n.left.val
            if   n.left.left : s+=self.sumallchild(n.left) 

        if n.right : 
            s=s+n.right.val
            if   n.right.right : s+=  self.sumallchild(n.right)              

        return s 
           
        

if __name__ == '__main__':
    
    a=TreeNode(4)
    
    b=TreeNode(2)
    c=TreeNode(9)
    
    d=TreeNode(3)
    e=TreeNode(5)
    
    f=TreeNode(6)
    g=TreeNode(7)
    
    t=Tree(a)
    t.add_left(a, b)
    t.add_right(a, c)
    
    
    t.add_left(b, d)
    t.add_right(b,e)
    
    t.add_left(c,g)
    '''
    t.add_right(d,g)
    '''
    
    
   
    
    
    obj = Solution()
    print obj.f(a)
    #print obj.calc_tilt_1(a)
    #xprint obj.findTilt(a)
    
    
    