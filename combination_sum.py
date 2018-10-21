'''
Created on Jul 30, 2018

@author: aavinash

link::   https://leetcode.com/problems/combination-sum/description/
'''

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        
        for i in candidates:
            if i < target :
                if target%i == 0:
                    result.append([ i for i in range(target/i)])
                else:
                    rem = target - i 
                        
                    
        
        
        
        
        

if __name__ == '__main__':
    obj = Solution()
    obj.combinationSum([1,2,4,7],8)