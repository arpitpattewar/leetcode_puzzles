'''
Created on Jul 8, 2018

@author: aavinash

problem :  https://leetcode.com/problems/multiply-strings/description/
'''


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        total=0
        if len(num2)==1:
            for i in range(len(num1)-1,-1,-1):
                
                zeros_to_be_added = "".join([ "0" for j in range(len(num1)-1-i)])
                
                s = str(int(num1[i])*int(num2)) + zeros_to_be_added
                total +=int(s)
            return total   
    
        if len(num2) > 1:
            total = 0 
            for i in range(len(num2)-1,-1,-1):
                print i
                zeros_to_be_added = "".join([ "0" for j in range(len(num2)-1-i)])
                total += int(str (self.multiply(num1, num2[i])) + zeros_to_be_added)
            return total
        
        
    def multiply1(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        total=0
        if len(num2)==1:
            for i in range(len(num1)-1,-1,-1):
                
                zeros_to_be_added = "".join([ "0" for j in range(len(num1)-1-i)])
                
                s = str(int(num1[i])*int(num2)) + zeros_to_be_added
                total +=int(s)
            return total   
    
        if len(num2) > 1:
            total = 0 
            for i in range(len(num2)-1,-1,-1):
                print i
                zeros_to_be_added = "".join([ "0" for j in range(len(num2)-1-i)])
                total += int(str (self.multiply(num1, num2[i])) + zeros_to_be_added)
            return total        
                 
                
                
if __name__ == '__main__':
    obj = Solution()
    print obj.multiply("223323424234","1000000000000000000000000000000000000")