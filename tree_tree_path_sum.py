'''
Created on Oct 20, 2018

@author: aavinash

link :  https://leetcode.com/problems/path-sum/

Solution link :  https://leetcode.com/problems/path-sum/discuss/36486/Python-solutions-(DFS-recursively-DFS%2Bstack-BFS%2Bqueue)
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def hasPathSum_1(self, root, sum1):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root : return 0
        for j in self.helper(root):
            if type(j) is not list : 
                if j==sum1 : return True
                else:return False
            else :
                if sum(self.flatten(j)) == sum1: return True
        return False 
    
    def helper(self, root):
        r=[]
        
        if root.left:
            print [root.val]+self.helper(root.left)
            r.extend( [ [root.val] +[i] for i in  self.helper(root.left)  ])
            #rr.append([i for i in [root.val]+self.helper(root.left)])
   

        if root.right:
            print [root.val]+self.helper(root.right) 
            #rl.append([i for i in [root.val]+self.helper(root.right)])
            r.extend( [ [root.val] +[i] for i in  self.helper(root.right)  ])
                  

        if not root.left and not root.right:
            return [root.val] 

        return  r
    
    def flatten(self, input):
         result = []
         for i in input:
             if type(i) is not list :
                 result.append(i)
             else:
                 result = result + self.flatten(i)
         return result  
     
     

    def hasPathSum_2(self, root, sum):
        if not root:
            return False

        if not root.left and not root.right and root.val == sum:
            return True
        
        sum -= root.val

        return self.hasPathSum_2(root.left, sum) or self.hasPathSum_2(root.right, sum) 
    
    
        

    def hasPathSum_with_stack(self, root, sum):  

        stack=[(root,root.val)] 

        sl,sr=0,0 
        
        while stack:
            #print stack
            head = stack.pop();
            #print sl,sr
            #print "head is {}".format(head[0].val)
            if head[0].left:
                stack.append((head[0].left, head[1] + head[0].left.val))

            if head[0].right:
                stack.append((head[0].right,head[1] + head[0].right.val) )  
                 
            if not  head[0].right and not head[0].left:
                if head[1]==sum : return True
        return False
                                 
                 
                
                
                
    
    
         
        

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
    #print obj.hasPathSum_2(a1,31)
    print obj.hasPathSum_with_stack(a1,14)
    
    
        
        