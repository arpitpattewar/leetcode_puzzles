'''
Created on Nov 14, 2018

@author: aavinash

link : https://leetcode.com/problems/remove-nth-node-from-end-of-list/
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
    
    
        hd=head
        cs=1
        cf=1
        slow = head
        while head:
            if slow.next: slow=slow.next
                
            if head.next : 
                head = head.next
                if head.next:
                    head = head.next
                    cf+=2
                    cs+=1
                else:
                    cf+=1
                    break
            else:
                break    

        if cf ==1 : return None  
        
        if (cf - n) > cs :
            counter= (cf - n) -cs
            cur = slow
            prev = slow
            for i in range(counter):
                prev = cur
                cur = cur.next
                
            prev.next = cur.next    

        
        else :
            cur = hd
            prev = hd

            if (cf - n) == 0:
                head = hd.next
                hd=head

            else:    
                for i in range(cf - n):
                    prev = cur
                    cur = cur.next
                    
                if cur.next :
                    prev.next = cur.next  
                else:
                    prev.next = None
                        
        return hd 
            
           
    def display(self, head):
       head = head

       while head :
               print head.val
               if  head.next : head = head.next
               else: break
       else: print "Empty linkedlist or loop exists"    
        
        

if __name__ == '__main__':
    
    a = ListNode(1)
    b= ListNode(2)
    a.next = b
    c =ListNode(3)
    b.next = c
    
    d=ListNode(4)
    c.next = d
    e=ListNode(5)
    d.next = e
    f=ListNode(6)
    e.next = f
    g=ListNode(7)
    f.next = g
    h=ListNode(8)
    
    g.next = h
    
    obj =Solution()
    
    #obj.reorderList(a)
    obj.removeNthFromEnd(g,2) 
    
    obj.display(g)

            
        
        
        
        
                               