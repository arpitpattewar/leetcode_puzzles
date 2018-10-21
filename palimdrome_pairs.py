'''
Created on Sep 12, 2018

@author: aavinash 
link : https://leetcode.com/problems/palindrome-pairs/description/

'''

#
#To understand solution given at  https://leetcode.com/problems/palindrome-pairs/discuss/79195/O(n*k2)-java-solution-with-Trie-structure
#


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        


        words = {word: i for i, word in enumerate(words)}
        valid_pals = []
        for word, k in words.iteritems():
            print "\n\nCheck for word {}".format(word)
            n = len(word)
            for j in range(n+1):
                pref = word[:j]
                suf = word[j:]
                
                if self.is_palindrome(pref):
                    print "pref:{},suf:{}".format(pref,suf)
                    back = suf[::-1];print "back+suf:{}".format(back)
                    if back != word and back in words:
                        valid_pals.append([words[back],  k])
                if j != n and self.is_palindrome(suf) :
                    print "pref:{},suf:{}".format(pref,suf)
                    back = pref[::-1];print "back+pref:{}".format(back)
                    if back != word and back in words:
                        valid_pals.append([k, words[back]])
        return valid_pals


    def is_palindrome(self, check):
        return check == check[::-1]
            
        
        
        
        

if __name__ == '__main__':
    obj = Solution()
    input1=["abcd","dcba","lls","s","sssll","xxxxxdcba"]
    input2=["bat","tab","cat","ta"]
    input3=["aaaa","aa","ba","aba","xxxaba"]
    print obj.palindromePairs(input3)