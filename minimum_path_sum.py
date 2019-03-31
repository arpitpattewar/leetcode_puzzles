'''
Created on Feb 3, 2019

@author: aavinash
link :   https://leetcode.com/problems/minimum-path-sum/

'''

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid) 
        col = len(grid[0]) 
        rw=0
        cl=0
        result = [(rw,cl)]
    
        
        while rw < rows or cl < col :
            if rw < rows and cl < col:
                move_set = [(rw+1,cl),(rw,cl+1)]
                
            if rw < rows and cl == col:
                move_set = [(rw+1,cl),(rw,cl)]
                
            if rw == rows and cl < col:
                move_set = [(rw,cl),(rw,cl+1)]                
                
                
                    
            
            tmp =[]
            for i in move_set:
                for j in result:
                    tmp = tmp + [i,j]
            result = tmp   
            rw+=1
            cl+=1
            
        return result            
        
        

            
            
    def traverse_matrix(self, grid, row, col):
        sumd = []
        sumr=[]
        if row+1 < len(grid):
            #sumd = sumd + [grid[row][col] ,self.traverse_matrix( grid, row+1, col)]
            #sumd.append(grid[row][col])
            sumd.append(self.traverse_matrix( grid, row+1, col) + grid[row][col])
            
        if col+1 < len(grid[0]): 
            sumr.append(grid[row][col]+self.traverse_matrix( grid, row, col+1) )
            
        if col+1 ==  len(grid[0]) and row+1 == len(grid):
            return grid[col][row]
        
        
        return  sumd,sumr  
             
                     
            
            
        
        
if __name__ == '__main__':    
    
    obj = Solution()
    print obj.minPathSum([[1,2,3,4]])
        