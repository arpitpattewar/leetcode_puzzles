'''
Created on Nov 18, 2018

@author: aavinash

link:  https://leetcode.com/problems/remove-duplicates-from-sorted-list/

'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    
    def display(self, head):
       head = head

       while head :
               print head.val
               if  head.next : head = head.next
               else: break
       else: print "Empty linkedlist or loop exists"    
        
            
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        prev = None
        if head :
            while True:
    
                if prev and prev.val == cur.val:
                    if cur.next:
                        prev.next = cur.next
                        cur = cur.next
                    else:
                        prev.next = None
                        break
                else:
                    prev = cur
                    if cur.next : cur = cur.next
                    else:
                        break  
            return head 
    
    def deleteDuplicatesSpec(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        Similar question :   https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/submissions/
        """
        cur = head
        prev = None
        prev_1 = None
        dup_mode_started = False
        if head :
            while True:
    
                if prev and prev.val == cur.val:
                    dup_mode_started = True
                    if cur.next: cur = cur.next
                    else: 
                        #prev.next = None
                        if prev_1: 
                            prev_1.next = None
                        else:
                            head = None    
                        break
                else:
                    if dup_mode_started :
                        dup_mode_started = False
                        if  prev_1:
                            #print prev_1.val,cur.val
                            prev_1.next = cur
                            cur = prev_1
                        else:
                            #print prev_1,cur.val
                            head = cur  
                            cur = head
                            prev = None
                            prev_1 = None  
                            
                    prev_1 = prev    
                    prev = cur
                    
                    if cur.next : 
                        cur = cur.next
                    else:
                        break         
        return head     
    
if __name__ == '__main__':
    
    a = ListNode(1)
    b= ListNode(5)
    a.next = b
    c =ListNode(4)
    b.next = c
    
    d=ListNode(4)
    c.next = d
    e=ListNode(4)
    d.next = e
    f=ListNode(6)
    e.next = f
    g=ListNode(6)
    f.next = g
    h=ListNode(8)
    
    g.next = h
    
    obj =Solution()
    
    #obj.reorderList(a)
    obj.display( obj.deleteDuplicatesSpec(a)) 
    
    #obj.display(a)
    