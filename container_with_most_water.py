'''
Created on Sep 9, 2018

@author: aavinash

link :    https://leetcode.com/problems/container-with-most-water/description/
'''


class Solution(object):
    
    def maxArea(self, A): 
        l = 0
        r = len(A) -1
        area = 0
          
        while l < r: 
            area = max(area, min(A[l],  A[r]) * (r - l)) 
            if A[l] < A[r]: 
                l += 1
            else: 
                r -= 1
        return area 
    
    
    def maxArea_1(self, height):
        L, R, width, res = 0, len(height) - 1, len(height) - 1, 0
        for w in range(width, 0, -1):
            if height[L] < height[R]:
                res, L = max(res, height[L] * w), L + 1
            else:
                res, R = max(res, height[R] * w), R - 1
        return res    

        
if __name__ == '__main__':
    obj = Solution()
    input = [1,8,6,2,5,4,8,3,7]
    input_1 = range(12)
    input_2 = [14,13,12,11,10,11]
    input_3 = [12,10]
    input_4=[1,2,1]
    input_5=[2,3,4,5,18,17,6]
    print obj.maxArea(input_5)
