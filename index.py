'''
Created on Jul 16, 2018

@author: aavinash

link:  https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
'''



class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=[]
        #if len(nums) == 1 and nums[0] == target : return [0,0]
        #else:
        for i in range(len(nums)):
            if nums[i] == target:
                l.append(i)
                
        if len(l) >= 2 :
            return [l[0],l[-1]]
        if len(l) == 1:
            return [l[0],l[0]] 
        else :
            return [-1,-1]       
                
        

if __name__ == '__main__':
    s=[5,7,7,7,7,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,10]
    a=Solution()
    print a.searchRange(s,8)
    