'''
Created on Sep 2, 2018

@author: aavinash

link : https://leetcode.com/problems/next-greater-element-iii/description/
'''

#
# Better solution to be find by others
#

class Solution(object):
    def helper(self, n):

        if  len(n) == 2: 
            rev = int(n[::-1]) 

            return -1 if rev <= int(n) else rev        
        else:
            first = n[0]
            d= dict([ (int(i)-int(first), int(i)) for i in n[1:]  if int(i) - int(first) > 0])

            if d:

                next_high = sorted(d.keys())[0]
                idx = n.index(str(d[next_high])) 
                result = n[idx] + "".join(sorted(n[:idx]+n[idx+1:]))
                return result   
            else :
                return -1        
        
    
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        n=str(n)
        if len(n) == 1 : return -1
        else:
            
            last_digits = 2
            while len(str(n)) >= last_digits :
                initial,last = n[:-1*last_digits], n[-1*last_digits:]
                updated = self.helper(last)
                
                if updated == -1 :
                    last_digits +=1 
                else:
                    final= int("{}{}".format(initial, updated )) 
                    return     final if final < 2147483647 else -1
                     
            return -1
            
            
        
        
if __name__ == '__main__':
    obj = Solution()
    print obj.nextGreaterElement(19499)