'''
Created on Mar 3, 2019
@author: aavinash
link:https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
'''
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution(object):
    
    def flattene_stack(self, head):
       if head: 
        stack = [head]
        result = None
        prev = None
        while stack:
            print "length of stack is {}".format(len(stack))
            head = stack.pop()
            if not result : 
                result = head
                result.prev = prev
                if head.next : stack.append(head.next)
                if head.child : stack.append(head.child)
                hh = result
            else:
                
                if head.child :
                    #prev = head
                    if head.next : stack.append(head.next)
                    result.next = head
                    result = result.next
                    prev = head
                    stack.append(head.child)
                else:    
                    prev = result
                    #head = stack.pop()
                    print "Adding {}".format(head.val)
                    result.next = head
                    result = result.next
                    result.prev = prev
                    if head.next :
                        prev = head
                        stack.append(head.next)
        return hh            
                
 
    def flatten_3(self, head):
        if not head:
            return
        
        dummy = Node(0,None,head,None)     
        stack = []
        stack.append(head)
        prev = dummy
        
        while stack:
            root = stack.pop()

            root.prev = prev
            prev.next = root
            
            if root.next:
                stack.append(root.next)
                root.next = None
            if root.child:
                stack.append(root.child)
                root.child = None
            prev = root        
            
        
        dummy.next.prev = None
        return dummy.next 
 
    
    def flattene_stack_1(self, head):
       if head: 
        stack = [head]
        result = None
        prev = None
        while stack:
            print "length of stack is {}".format(len(stack))
            head = stack.pop()
            if not result : 
                result = head
                result.prev = prev
                if head.next : stack.append(head.next)
                if head.child : stack.append(head.child)
                hh = result
            else:
                
                if head.child :
                    #prev = head
                    if head.next : stack.append(head.next)
                    result.next = head
                    result = result.next
                    prev = head
                    stack.append(head.child)
                else:    
                    prev = result
                    #head = stack.pop()
                    print "Adding {}".format(head.val)
                    result.next = head
                    result = result.next
                    result.prev = prev
                    if head.next :
                        prev = head
                        stack.append(head.next)
        return hh      
    
    
    def traverse(self,a):
        while True:
            if a : 
                print a.val 
                a = a.next
    
            else:
                #print a.val 
                break    
                   
                  
        
if __name__ == '__main__':
    obj = Solution()
    #obj.flatten(head) 
    
    a=Node(1, None, None, None)
    b= Node(2, None, None, None)
    c= Node(3, None, None, None)
    
    d= Node(4, None, None, None)
    e= Node(5, None, None, None)
    f= Node(6, None, None, None)
    g= Node(7, None, None, None)
    h= Node(8, None, None, None)
    j= Node(9, None, None, None)
    
    x= Node(11, None, None, None)
    y = Node(12, None, None, None)
    z= Node(13, None, None, None) 
    v= Node(100, None, None, None) 
    u= Node(109, None, None, None) 

    
    '''
     1   2   3   6   8 
     a-->b-->c-->f-->h
             |
             d4
             |
             e5
             |
             j9
          
           
    '''      
    
    a.next = b
    b.prev =a 
    b.next= c 
    c.prev = b 
    
    c.child = d 
    d.next = e
    e.prev = d
    e.next = j
    j.prev=e
     
    
    c.next = f
    f.prev = c
    f.next =h 
    h.prev =   f
    
    
    a.child = x 
    x.child = y 
    y.child = z

     
     
     
    
    
    
    

    

    
    
    
    '''
    b= Node(1, a, None, None)
    b= Node(1, a, None, None)
    b= Node(1, a, None, None)
    b= Node(1, a, None, None)
    '''
    #
    a=obj.flatten_3(a)
    
    
    ba=obj.flattene_stack(a)
    
    obj.traverse(ba) == obj.traverse(a)

    #print h.val,h.prev.val

    
           
    
    
    
    
    
    
    
    
    
    
         