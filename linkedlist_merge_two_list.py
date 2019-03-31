'''
Created on Feb 9, 2019

@author: aavinash

link: https://leetcode.com/problems/merge-two-sorted-lists/
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


        
class Solution(object):
                  
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rl = None
        if (l1 and not l2) or (l2 and not l1) :
            return l1 or l2
        elif not (l2 and  l1): return None
        
        else:
        
            while True:
                if l1 and l2:
                    if l1.val < l2.val : 
                        if not rl:
                            #print "Head is set to {}".format(l1.val)
                            rl = ListNode(l1.val)
                            head = rl
                        else:
                            #print "Adding l1 {}".format(l1.val)
                            rl.next=ListNode(l1.val)
                            rl = rl.next
                        l1=l1.next                    
                    else:
                        if not rl:
                            #print "Head is set to {}".format(l2.val)
                            rl = ListNode(l2.val)
                            head = rl
                        else:
                            #print "Adding l2 {}".format(l2.val)
                            rl.next=ListNode(l2.val)
                            rl = rl.next
                        l2=l2.next
                else:
                    left_over = l1 or l2
                    rl.next  =  left_over
                    break
            return head                     
                        
    def mergeTwoLists_rec(self,l1,l2):
        rl = None
        if (l1 and not l2) or (l2 and not l1) : return l1 or l2
        elif not (l2 and  l1): return None
        else:
                if l1 and l2:
                    if l1.val < l2.val : 
                            rl = ListNode(l1.val)
                            rl.next = self.mergeTwoLists_rec(l1.next,l2)                   
                    else:
                            rl = ListNode(l2.val)
                            rl.next = self.mergeTwoLists_rec(l2.next,l1) 
                else:
                    rl.next  =  l1 or l2           
        return rl     
    
    
    def mergeKLists(self, linkedlistArray):
        l=len(linkedlistArray) 
        if not linkedlistArray : return None
        else:
            if l > 2 : 
                return self.mergeTwoLists_rec( self.mergeKLists(linkedlistArray[:l/2]), self.mergeKLists(linkedlistArray[l/2:]) )
            else :  return self.mergeTwoLists_rec(linkedlistArray[0], None if l ==1 else  linkedlistArray[1])  
                
            
            
    def mergeKLists_leetcode_solution(self, lists):
        from heapq import heappush, heappop, heapreplace, heapify
        dummy = node = ListNode(0)
        h = [(n.val, n) for n in lists if n]
        #print h
        heapify(h);
        while h:
            print h
            v, n = h[0]
            if n.next is None:
                heappop(h) #only change heap size when necessary
                print "after popping {}".format(h)
            else:
                heapreplace(h, (n.next.val, n.next))
            node.next = n
            node = node.next
        return dummy.next           
            
        
        
if __name__ == '__main__':
    '''
    Test cases
    [1,2,3] [3,10,99]
    [-1,0,34][23,55,698,654654]
    [0][0]
    [][1]
    [][]
     '''      
    
    a = ListNode(-12)
    b= ListNode(17)
    c= ListNode(57)
    d =  ListNode(77)
    
    a.next= b
    b.next =c
    c.next = d 
     
    
    e= ListNode(-9)
    f = ListNode(31) 
    
    e.next = f
    
    g=ListNode(3)
    h=ListNode(44)
    i =  ListNode(78) 
    
    g.next = h
    h.next = i  
    
    obj = Solution()

    #r = obj.mergeTwoLists_rec(a,g)
    #r= obj.mergeKLists([a,e,g])
    r=obj.mergeKLists_leetcode_solution([a,e,i])
    
    while r:
        print r.val
        r=r.next
        
    
    
    