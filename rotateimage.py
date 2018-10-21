'''
Created on Jul 10, 2018

@author: aavinash
link :   https://leetcode.com/problems/rotate-image/description/

[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
'''



class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return matrix
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if i < j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            print matrix        
        
        for row in matrix:
            row.reverse()
        return matrix
                    
                            

if __name__ == '__main__':
    t1=[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

    obj = Solution()
    print obj.rotate(t1)