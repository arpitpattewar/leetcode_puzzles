'''
Created on Sep 13, 2018

@author: aavinash

link:  https://leetcode.com/problems/target-sum/discuss/97343/Python-DP
is Dynamic solution possible:  yes ,https://leetcode.com/problems/target-sum/solution/
'''


class Solution(object):
    def findTargetSumWays(self, nums, S):
        d = {nums[0]:1,-nums[0]:1}  if nums[0] != 0 else {0: 2};print d
        for n in range(1,len(nums)):
            
            tmp={}
            for k in d:
                tmp[k+nums[n]] = tmp.get(k+nums[n],0) + d.get(k,0)
                tmp[k-nums[n]] = tmp.get(k-nums[n],0) + d.get(k,0)
            d=tmp
            print d,nums[n]
        return d.get(S,0)   
    
         
    #
    #One small and clean solution
    #     

    def findTargetSumWays_2(self, nums, S):
        from collections import defaultdict
        memo = {0: 1}
        for x in nums:
            m = defaultdict(int)
            for s, n in memo.iteritems():
                m[s + x] += n
                m[s - x] += n
            memo = m
        return memo[S]         
                
                
            

    
    
if __name__ == '__main__':
    obj = Solution()
    a=[1,2,3,4,5,-4,-6,-23,0,12,23,-8]
    b=[1,1,1,2,3]
    c=[0,10,0,0,0,0,0,1]
    print obj.findTargetSumWays(c,-9)
    #print obj.findTargetSumWays_1(b,4)