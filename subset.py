'''
Created on Feb 12, 2019

@author: aavinash

link: https://leetcode.com/problems/subsets/
'''

class Solution(object):

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums:
            r=[]
            for i in range(0, len(nums)+1):
                for k in self.combb(nums,i):
                    r.append(k)
                
            return r+[[]]   

    
    
    def combb(self, nums, size):
     if  nums :
        if size==0 : return []
        if size == 1 : return [ [i] for i in nums]
        if size == 2: 
            r=[]
            
            for i in nums :
                for j in nums :
                    if i!=j :
                        if ([i,j] and [j,i]) not in r: r.append([i,j])
            return r        
                        
        if size == len(nums) : return [nums]
        else:
            t=[]
             
            for j in self.combb(nums,size-1):
                 for i in nums :
                      if i not in j: 
                          if sorted(j+[i]) not in t:
                           t.append(sorted(j+[i]))
            return t          
                     
                
            #return [ j+[i]   for j in self.combb(nums,size-1) for i in nums  if i not in j ]
                    
   
        

if __name__ == '__main__':
    obj =Solution()  
    #print obj.combb([1,9,0,3,4,5,6,7,8,9,11],2) 
    print obj.subsets([1,2,3,4])     
        