'''
Created on Sep 10, 2018

@author: aavinash

link::   https://leetcode.com/problems/longest-palindromic-substring/description/
'''
class Solution(object):
    
    
    def longestPalindrome(self, s):
        """Solution from another users
        """
        res = ""
        for i in xrange(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res
 
    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
            print l,r
        return s[l+1:r]
    
    
        
    def longestPalindrome_1(self, s):
        """
        Ypur solution
        :type s: str
        :rtype: str
        """
        if len(s)==1: return s
        if len(s)==0 : return ""

        con = 0
        leng = len(s)-1
        result = ""
        
        while con < leng:
            current = s[con]
            st,end=con,leng
            while st <= end:
                l=0
                if s[end] != current: end-=1
                else:
                    word = s[con:end+1]
                    l = len(word)

                    if word == word[::-1]: 
                        if len(result) < l : result = word
                        con=end
                    end-=1  
            con+=1         
 
        return result if len(result) >0 else s[0]             
                        
            


if __name__ == '__main__':
    obj =Solution()
    print obj.longestPalindrome("abacab")