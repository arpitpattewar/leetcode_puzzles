class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        #Without split statement in python
        c=0
        flag=False
        for i in range(len(s)-1,-1,-1):
            if  s[i]!=" " :
                c+=1
                flag=True
            else:
                if flag:
                    break
        return c
        '''
  
        return len((filter(lambda x:x, s.split(" ")) or [""])[-1])
        


