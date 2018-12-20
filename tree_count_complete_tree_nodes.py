
"""
link: 
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution_1(object):
    

    def countNodes(self, head):
        
        if head:

            h = self.height(head)
            print len(self.display_leaves(head))
            print h            
            return  pow(2,h-1)-1 + len(self.display_leaves(head))  
        #elif head==[]:return 0
        else : return 0
        
        
        
    def height(self, head=None ):
        if not head : return 0
        
        hl,hr=0,0
        #if not head.left and head.right : return -1
        if head.left : hl=hl +1 + self.height(head.left)
        if head.right : hr=hr+1 + self.height(head.right)
        if not head.right and not  head.left : return 1
        return max(hr,hl)
    
    
    
        
    def display_leaves(self, head=None):
        l=[]
        
        if not head  : return []
        if head.left :  l=l+self.display_leaves(head.left)
        if head.right :  l=l+self.display_leaves(head.right)
        if not head.left and not head.right : l.append(head.val)
        return   l
    
    def bredth_first_traversal(self, head):
        stack = [] 
        if not head : return   
        if head.left: stack.append(head.left)
        if head.right: stack.append(head.right)
        
        while stack:
            for i in stack:
                print i.val  
                              
class Solution_2:
        # @param {TreeNode} root
        # @return {integer}
        def countNodes(self, root):
            if not root:
                return 0
            leftDepth = self.getDepth(root.left)
            rightDepth = self.getDepth(root.right)
            if leftDepth == rightDepth:
                return pow(2, leftDepth) + self.countNodes(root.right)
            else:
                return pow(2, rightDepth) + self.countNodes(root.left)
    
        def getDepth(self, root):
            if not root:
                return 0
            print root.val
            return 1 + self.getDepth(root.left)        
        
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # O(logn logn)
        h = self.height(root)
        nodes = 0
        while root:
            print root.val,nodes,h
            if self.height(root.right) == h - 1:
                nodes += 2 ** h  # left half (2 ** h - 1) and the root (1)
                root = root.right
            else:
                nodes += 2 ** (h - 1)
                root = root.left
            h -= 1
        return nodes        

    def height(self, root):
        return -1 if not root else 1 + self.height(root.left)                  
    
    
    
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
    
    
    '''
    a1.right.left = e
    a1.right.right = f
    
    
    g=TreeNode(8)
    h=TreeNode(9)
    i=TreeNode(8)
    j=TreeNode(9)
    
    a1.left.right.left=g
    a1.left.right.right=h
    
    a1.right.left.left = j
    a1.right.left.right = i 
    '''
    obj = Solution()

    print obj.height(a1);print obj.height(a1.right);print obj.height(a1.left)
    print obj.countNodes(a1)
    
      