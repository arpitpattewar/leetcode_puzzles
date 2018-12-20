'''
Created on Nov 2, 2018

@author: aavinash
Link:   https://leetcode.com/problems/linked-list-cycle-ii/

'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
         if not head :return None
         d=[]
         first=head

         while True:
             if first in d: return first
             else: d.append(first) 

             if  first.next:
                 first=  first.next
             else:
                return None
            
            
            
    def detectCycle_leetcode(self, head):
        try:
            fast = head.next
            slow = head
            while fast is not slow:
                fast = fast.next.next
                slow = slow.next
                print "from first while {},{}".format(fast.val, slow.val)
        except:
            # if there is an exception, we reach the end and there is no cycle
            return None

        # since fast starts at head.next, we need to move slow one step forward
        print head.val, slow.val
        slow = slow.next
        while head is not slow:
            head = head.next
            slow = slow.next
            print head.val, slow.val

        return head.val            
             
 

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
    
    h.next = a

    
    obj = Solution()
    print obj.detectCycle_leetcode(a)