'''
Created on Aug 12, 2018

@author: aavinash
link : https://leetcode.com/problems/integer-to-roman/description/
'''



class Solution(object):
    def lookup(self, input):
        """
        :type num: int
        :rtype: str
        """
        d ={1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}
        
        if d.has_key(input):
            return d[input]
        else:
        
            if len(str(input)) == 1:
                if input < 4 : return d[1]*input
                else: return d[5]+d[1]*(input-5)
                
            if len(str(input)) == 2:
                if input < 40 : return d[10]*(input/10)
                else: return d[50]+d[10]*((input/10)-5)                 
            
            if len(str(input)) == 3:
                if input < 400 : return d[100]*(input/100)
                else: return d[500]+d[100]*((input/100)-5) 
                
            if len(str(input)) == 4:  return d[1000]*(input/1000)
            
    def intToRoman(self, num): 
        num = str(num)
        #print [ int(num[i])*pow(10,len(num)-1-i)  for i in range(len(num))]
        return "".join([ self.lookup(int(num[i])*pow(10,len(num)-1-i))  for i in range(len(num))]) 
        
        
     

if __name__ == '__main__':
    o = Solution()
    o.intToRoman(2300)