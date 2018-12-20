'''
Created on Nov 5, 2018

@author: aavinash

link: https://leetcode.com/problems/reorder-list/
'''


class ListNode(object):
    def __init__(self, x):
        self.data = x
        self.next = None

class Solution(object):
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

    def reorderList(self, head):
        if head is None:
            return
        p = head
        q = head
        # slow pointer p and quick pointer q
        while q is not None and q.next is not None:
            q = q.next.next
            p = p.next
        # find middle
        mid = p.next;print mid.data
        p.next = None
        begin = head
        end = mid
        pre = None
        # reverse link
        while end is not None:
            temp = end.next
            end.next = pre
            pre = end
            end = temp
            
        self.display(head)    
        # merge link
        while pre is not None and begin is not None:
             a = pre.next
             b = begin.next
             begin.next = pre
             pre.next = b
             begin = b
             pre = a
        return

            
  
    
    def display(self, head):
       head = head

       while head :
               print head.data
               if  head.next : head = head.next
               else: break
       else: print "Empty linkedlist or loop exists"  
       
       
    def revlinkedlist(self, head):
        cur= head
        pre = None
        
        while cur.next:
            #print cur.data
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        



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
    obj.revlinkedlist(a) 
    
    obj.display(h)
    
        