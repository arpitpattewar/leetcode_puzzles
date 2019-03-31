'''
Created on Jan 29, 2019

@author: aavinash

link:  https://leetcode.com/problems/add-two-numbers/
'''



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    
        
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        nx1=l1
        nx2=l2
        res = None
        sum=0
        div=0
        while nx1 or nx2:
            sum = div + (nx1.val if nx1 else 0) + (nx2.val if nx2 else 0);print sum
            car = sum % 10
            div = sum/10
                  
            if not res:
                res = ListNode(car)
                head = res
            else:
                res.next =  ListNode(car)   
                res=res.next
                
            sum=0
            nx1=nx1.next if nx1 else None
            nx2=nx2.next if nx2 else None
        if div > 0 :res.next =   ListNode(div)  
        return head 
        
        
if __name__ == '__main__':
    
    a = ListNode(9)
    b = ListNode(6)

    
    a.next = b


    
    d = ListNode(5)
    e = ListNode(3)

    
    d.next = e
    #e.next = f 
    
    obj = Solution()
    l=obj.addTwoNumbers(a,d)
    r=[]
    while l:
        if l : 
            r.append(l.val)
            l=l.next
            
    print r        
            
        
    
    
    
    
    
            
