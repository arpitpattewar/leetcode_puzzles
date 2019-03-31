'''
Created on Feb 15, 2019

@author: aavinash

link:  https://leetcode.com/problems/number-of-islands/
'''

class Solution(object):
     def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid : return 0
        count =  0
        visited_islands=[]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]=="1":
                    #print "i={},j={}".format(i,j)
                    new_island = sorted(self.dfs_1(i,j,grid))
                    #print new_island
                    if new_island not in visited_islands:
                        visited_islands.append(new_island) 
                        count+=1
                    print   visited_islands  
        return count 
    
     def dfs_1(self, i, j, grid, cord=[]):
         possible_set = [ (i,j+1),(i,j-1),(i+1,j),(i-1,j),(i,j)]
         valid_set = [ (k,l) for k,l in possible_set 
                      if k in range(0,len(grid)) 
                       and 
                      l in range(0,len(grid[0])) ]
         #print "i={},j={}, valid_set={}".format(i,j,valid_set)
         for x,y in valid_set:
             if grid[x][y] == "1":
                 if [x,y] not in cord : 
                     cord.append([x,y])
                     self.dfs_1( x, y, grid, cord)
         return cord          
     

     def numIslands_2(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
            
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    print grid
                    #print self.dfs(grid, i, j)
                    count += 1
                #print count            
        return count
    
     def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)     
        
     def numIslands_3(self, grid):
        """"
         link : https://leetcode.com/problems/number-of-islands/discuss/56349/7-lines-Python-~14-lines-Java
        """
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = '0'
                map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
                return 1
            return 0
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))        
                      
                   

        


if __name__ == '__main__':
    obj= Solution()
    input_1 =[['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']]
    input_2=[['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '1', '1', '0', '0'], ['0', '0', '0', '1', '1']]
    input_3=[["1","0","1","1","0","1","1"]]
    '''
11110
11010
11000
00000

11000
11000
00100
00011

    '''
    print obj.numIslands_3  (input_3)
    
    #print obj.dfs_1(0, 0,input_1 )
    
            