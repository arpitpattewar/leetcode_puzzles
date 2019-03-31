'''
Created on Jan 26, 2019

@author: aavinash

link: https://leetcode.com/problems/add-two-numbers-ii/

'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    
    def pop(self, head):
        if head:
            h = head
            prev= None
            while True:
                if head.next : 
                    prev = head
                    head = head.next
                else:
                    if prev : prev.next = None
                    else : 
                        return head,None
                    return head,h
        else:
            return None,None
                
                    
    
    def addTwoNumbers(self, l1, l2):
        
        nx1,l1=self.pop(l1)
        nx2,l2=self.pop(l2)
        res = None
        sum=0
        div=0
        while nx1 or nx2:
            #print  nx1.val,nx2.val
            if not nx1 and nx2:
                 #nx1=ListNode(0)
                 sum  = nx2.val + div
            elif not nx2 and nx1: 
                #nx2=ListNode(0)    
                 sum  = nx1.val +  div  
            else:          
                sum  = nx1.val + nx2.val + div 
                   
            car = sum % 10
            div = sum/10

            if not res:
                res = ListNode(car)
                head = res
                sum=0
            else:
                tmp = head
                head =  ListNode(car)
                head.next = tmp 
                sum=0 
            nx1,l1=self.pop(l1)
            nx2,l2=self.pop(l2)  
            
        if div > 0 :
            tmp = head
            head =  ListNode(div);
            head.next =  tmp  
            #head.next = tmp                 
            
        return head 
    
    
        
if __name__ == '__main__':
    
    a = ListNode(9)
    b = ListNode(6)

    
    a.next = b


    
    d = ListNode(9)
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
                 