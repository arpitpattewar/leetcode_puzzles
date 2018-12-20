'''
Created on Nov 1, 2018

@author: aavinash

link: https://leetcode.com/problems/construct-string-from-binary-tree/

'''

from LeetCodeTree import TreeNode



class Solution(object):
    def tree2str_1(self, root):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not root : return ""
        rs=""
        rs = rs+ str(root.val)
        if root.left:
            rs = rs + "({})".format(self.tree2str(root.left))
        if root.right: 
            if not root.left: rs=rs + "()"
            rs = rs + "({})".format(self.tree2str(root.right)) 
        return rs
    
    
    def tree2str_2(self, root):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not root : return ""
        rs=[]
        rs.append(str(root.val))
        if root.left:
            rs.append("({})".format(self.tree2str(root.left)))
        if root.right: 
            if not root.left: rs.append("()")
            rs.append("({})".format(self.tree2str(root.right))) 
        return "".join(rs) 
    
    
    def tree2str(self, root):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not root : return ""
        rs=[]
        rs.append(str(root.val))
        if root.left:
            rs.append("({})".format(self.tree2str(root.left)))
        if root.right:     
            rs.append("{}({})".format( '()'  if not root.left else "" ,self.tree2str(root.right))) 
        return "".join(rs)   
    
    def tree2str_leetcode(self, t):
        """
        """
        if not t: return ''
        left = '({})'.format(self.tree2str(t.left)) if (t.left or t.right) else ''
        right = '({})'.format(self.tree2str(t.right)) if t.right else ''
        return '{}{}{}'.format(t.val, left, right)     
            
        
        
        
        
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
    
    a1.right.left = c
    
    a1.right.right = d
    
#     
#     a1.left.left.left = e
    a1.left.right = f
     
#      
#     g=TreeNode(8)
#     h=TreeNode(9)
#     i=TreeNode(8)
#     j=TreeNode(9)
#      
#     a1.left.left.left.left=g
#     a1.left.left.left.right=h
         
     
    obj = Solution()
    print obj.tree2str(a1)
            