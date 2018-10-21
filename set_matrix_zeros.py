'''
Created on Aug 4, 2018

@author: aavinash
'''

class Solution(object):
    
    def setZeroes_2(self, matrix):
            """
            :type matrix: List[List[int]]
            :rtype: void Do not return anything, modify matrix in-place instead.
            """
            row_flag = False
            col_flag = False
            
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    print matrix
                    print i,j
                    if i == 0 and matrix[i][j] == 0:
                        row_flag = True
                    if j==0 and matrix[i][j] == 0:
                        col_flag = True
                    if matrix[i][j] == 0:
                        matrix[0][j] = 0
                        matrix[i][0] = 0
                        
            
            for i in range(1, len(matrix)):
                for j in range(1, len(matrix[0])):
                    if matrix[0][j] == 0 or matrix[i][0] == 0: 
                        matrix[i][j] = 0 
            if row_flag == True:
                for i in range(len(matrix[0])):
                    matrix[0][i] = 0
            
            if col_flag == True:
                for i in range(len(matrix)):
                    matrix[i][0] = 0
                    
            return matrix        
                    
    def setZeroes(self, input):
        row_index=[]
        column_index=[]
        for i in range(len(input)):
            c=input[i].count(0)
            if c >0: 
                row_index.append(i)
                column_index.append(input[i].index(0))
                    
        #print   row_index,column_index           
                    
        for i in range(len(input)):
            for j in range(len(input[i])):
                if i in row_index or j in column_index:
                    #print input[i][j]
                    input[i][j] = 0
                    #print input
        return input                   
                
                             
        
    def setZeroes_1(self, input):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        
        
        Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
        """
        row_index=[]
        column_index=[]
        
        for i in range(len(input)):
            for j in range(len(input[i])):
                if input[i][j] == 0 :
                    if i not in row_index : row_index.append(i)
                    if j not in column_index : column_index.append(j)
                    
                           
        for i in range(len(input)):
            for j in range(len(input[i])):
                if i in row_index or j in column_index:
                    #print input[i][j]
                    input[i][j] = 0
                    #print input
        return input   
    
    
    def setZeroes_4(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        col0, rows, cols = 1, len(matrix), len(matrix[0])

        for i in xrange(0, rows):
            if matrix[i][0] == 0:
                col0 = 0
            for j in xrange(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        #print matrix            

        for i in xrange(rows-1, -1, -1):
            for j in xrange(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            #print matrix        
            if col0 == 0:
                matrix[i][0] = 0

        print matrix    
                         
        
        
        
        
        
        
if __name__ == '__main__':
    obj = Solution()
    input_1=[
  [1,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
    input_3=[
        [1,3,5,1,5,6,7,8,9,6,5,3,2],
        [2,0,1,3,0,0,0,4,4,4,4,4,4],
        [2,4,3,0,1,1,1,1,1,1,1,1,1]]
    
    
    input_2=[[1,1,1],[1,0,1],[1,1,1]]
    print obj.setZeroes_4(input_1)
