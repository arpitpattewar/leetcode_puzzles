'''
Created on Aug 30, 2018

@author: aavinash

link :  https://leetcode.com/problems/koko-eating-bananas/description/
'''
import time

class Solution(object):
        
    
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        
                           
    def minEatingSpeed_1(self, piles, H):
        low, high =  sum(piles)/H, max(piles)
        while low < high:
            #print low,high
            mid = (low + high) // 2;print low,high,mid
            if self.apply_check(piles, mid, H) <= H:
                high = mid 
            else:
                low = mid +1
        return low
        
        
    def apply_check(self,piles,av,H):
        sum1=0
        for i in piles:
            if i >0:
                qot = i/av
                reminder = i%av
                if reminder :
                    sum1=sum1+qot + 1
                else:
                    sum1=sum1+qot
        return sum1            
       
        #if sum1 == H : return av        
            
        
        
        
if __name__ == '__main__':
    obj =  Solution()
    #print obj.minEatingSpeed(piles = [3,6,7,11], H = 8)                            
    #print obj.minEatingSpeed(piles = [30,11,23,4,20], H = 6) 
    print obj.minEatingSpeed_1(piles =[332484035, 524908576, 855865114, 632922376, 222257295, 690155293, 112677673, 679580077, 337406589, 290818316, 877337160, 901728858, 679284947, 688210097, 692137887, 718203285, 629455728, 941802184],H=823855818)
                        
                    
            
            