'''
Created on Jul 5, 2018

@author: aavinash

Problem link : https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
'''



class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 : return 0
        else:
            substr=""
            ready=""
            for i in range(len(s)):
                if s[i] not in substr:
                    substr =substr+s[i]
                else:
                    if len(ready) < len(substr):
                        ready=substr 
                                       
                    substr = substr[substr.index(s[i])+1:]+s[i]
                    if len(ready) < len(substr):
                        ready=substr   
                        
            print ready, substr               
            return  max(len(ready), len(substr)) 
        



if __name__ == '__main__':
    obj = Solution()
    print obj.lengthOfLongestSubstring("vbxpvwkkteaiob")
    print obj.lengthOfLongestSubstring("anviaj")
    print obj.lengthOfLongestSubstring("cdd")
    print obj.lengthOfLongestSubstring("wwwewrwertyjyiunbrtecervh")
    