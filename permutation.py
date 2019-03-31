'''
Created on Sep 15, 2018

@author: aavinash

link: https://leetcode.com/problems/permutations/description/

'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)==1 : return [nums]
        else:
            r={}
            for i in range(len(nums)):
                tmp = [ nums[k] for k in range(len(nums)) if i!=k ]
                for j in self.permute(tmp): 
                    k="{}{}".format([nums[i]],j)
                    v=[nums[i]]+j
                    r[k] =r.get(k,v)
        return r.values()
    
    def permute_1(self, nums):
        return nums and [p[:i] + [nums[0]] + p[i:]
                         for p in self.permute(nums[1:])
                         for i in range(len(nums))] or [[]]    




if __name__ == '__main__':
    obj = Solution()
    print obj.permute([2,2,3])