'''
Created on April 30, 2019

@author: aavinash

link :  https://leetcode.com/problems/longest-consecutive-sequence/
'''
import sys

class Solution(object):

   def longestConsecutive(self, nums):
    nums = set(nums)
    best = 0
    for x in nums:
        if x - 1 not in nums:
            print x,best
            y = x + 1
            while y in nums:
                y += 1
            best = max(best, y - x)
    return best 

   def longestConsecutive_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        for i in nums:
            if not d.has_key(i):
                d[i]=1            
            prv= i-1
            nxt= i+1
            if d.has_key(prv):
                print "{} got prv {}".format(i, prv)
                #d[prv] +=1
                d[i] = d[i]+1 
                del d[prv]

            print d    

            if  d.has_key(nxt):
                print "{} got nxt {}".format(i, nxt)
                #d[nxt] +=1
                d[i] = d[i]+1
                del d[nxt]

            print d    

    
            print d
            
        #print d        
                            


        


if __name__ == '__main__':
    obj = Solution()
    test1=[100, 4, 200, 1, 3, 2]
    test2=[15,45,11,14,88,13,89,10,44,-23,12]
    test3=[-12,45,7,88,194,537,333,9467]
    input = [int(sys.argv[i]) for i in range(1,len(sys.argv))]
    print "input is {}".format(input)
    print obj.longestConsecutive(input)        
