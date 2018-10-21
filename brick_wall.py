'''
Created on Sep 4, 2018

@author: aavinash

link:   https://leetcode.com/problems/brick-wall/description/
'''
import collections


class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        d={}
        
        total_sum = sum(wall[0])
        for j in range(len(wall)):
            for k in [ sum(wall[j][:i+1]) for i in range(len(wall[j]))]:
                
                if d.has_key(k):
                    d[k] = d[k]+[j]
                else:
                    d[k]=[j]    

        if len(d) ==1 :   return len(wall)        

        else:
            if len(d) > 1 : del d[total_sum]
            result = map(len,d.values())   if len(d) > 1 else map(len,d.values())  
            return (len(wall) -max(result) )  if len(result) > 0  else len(wall)          

    def leastBricks_2(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        #d={}
        d = collections.defaultdict(int)
        total_sum = sum(wall[0])
        for j in range(len(wall)):
            for k in [ sum(wall[j][:i+1]) for i in range(len(wall[j]))]:

                    d[k] += 1

        print d
        if len(d) ==1 :   return len(wall)        

        else:
            if len(d) > 1 : del d[total_sum]
            result = map(len,d.values())   if len(d) > 1 else map(len,d.values())  
            return (len(wall) -max(result) )  if len(result) > 0  else len(wall)          
                
                               
               
               
               
                
                

    def leastBricks_1(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        d = collections.defaultdict(int)
        for line in wall:
            i = 0
            for brick in line[:-1]:
                i += brick
                d[i] += 1
        # print len(wall), d
        return len(wall)-max(d.values()+[0])                
        
        
        
        

if __name__ == '__main__':
    obj = Solution()
    t=[[1,2,2,1],
 [3,1,2],
 [1,3,2],
 [2,4],
 [3,1,2],
 [1,3,1,1]]
    u=[[1],[1],[1]]
    V=[[1,1],[2],[1,1]]
    w=[[7, 1, 2], [3, 5, 1, 1], [10]]
    print obj.leastBricks_2(t)
    