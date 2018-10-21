'''
Created on Aug 31, 2018

@author: aavinash

link :  https://leetcode.com/problems/product-of-array-except-self/description/
'''

class Solution(object):
    def productExceptSelf_2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = reduce(lambda x,y:x*y, nums)
        if nums.count(0) == len(nums): return [0 for i in nums]
        else :  return [p/i if not i ==0 else 1 for i in nums]  
        
    def productExceptSelf_1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [ reduce(lambda x,y:x*y,nums[:i]+nums[i+1:]) for i in range(len(nums))]   
    
    
    def productExceptSelf_3(self, nums):
        d={}
        p=1
        count_0 = nums.count(0)
            
        if count_0 :
            if count_0 > 1 : return [0 for i in nums]   
            if count_0 == 1: return [ 0 if i!=0 else p for i in nums ]
        else:
            for i in nums : p=p*i
            r=[]
            prev = 1
            for i in nums:
                p = (p/i)  * prev 
                prev= i
                r.append(p)       
        return r 
    
    def productExceptSelf_4(self, nums):
        """
        One of the solution from submitters
        """
        n = len(nums)
        res = [1] * n
        l = 0
        r = n - 1
        lval = 1
        rval = 1
        while r > -1:
            res[l] *= lval
            lval *= nums[l]
            l += 1
            
            res[r] *= rval
            rval *= nums[r]
            r -= 1
            

        return res    
            
        
        
        
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        
        """
        d={}
        for i in nums:
            d[i]=d.get(i, 0)+1

        r={}
        f=[]
        for i in nums:
            if not r.has_key(i):  f.append(self.get_product(i, d))
            else: f.append(r[i])
        return f        
            
          


    def get_product(self, input, d):
        p = 1
        for k,v in d.iteritems():
            if input !=k :
                #print k,v
                p = p *pow(k,v)
            else:
                #print "got it"
                p = p * pow((k if v > 1 else 1),(v-1 if v > 1 else 1))
        #print p    
        return p 
        


if __name__ == '__main__':
    obj =  Solution()
    print obj.productExceptSelf_3([1,2,3,4,5])