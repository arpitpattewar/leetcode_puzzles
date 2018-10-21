'''
Created on Sep 6, 2018

@author: aavinash
link ::  https://leetcode.com/problems/4sum-ii/description/
'''
import collections

class Solution(object): 
    
    def fourSumCount_1(self, A, B, C, D):
        AB = collections.Counter(a+b for a in A for b in B)
        return sum(AB[-c-d] for c in C for d in D)

                       
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        from collections import defaultdict
        if A == B == C ==D :return pow(len(A),4)
        d1,d2 = {},{}
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        length = len(A)
        for i  in range(length):
            for j in range(length):
                d1[(A[i] + B[j])*(-1)] += 1 
                d2[C[i] + D[j]] += 1 
        return   sum([d1[k]*d2[k] for k  in d1])
        
        
if __name__ == '__main__':
    obj = Solution()
    A = [ 1, 0,4]
    B = [-2,-1,3]
    C = [-1, 2,-2]
    D = [ 0, 2,-1]
    print obj.fourSumCount(A, B, C, D)
    