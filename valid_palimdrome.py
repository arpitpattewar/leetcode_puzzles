'''
Created on Dec 7, 2022

@author: aapattewar

link: https://leetcode.com/problems/valid-palindrome/

'''
import sys

class Solution(object):


	def isPalindrome_suggested(s):
		l, r = 0, len(s) - 1
		while l < r:
			if not s[l].isalnum():
				l += 1
			elif not s[r].isalnum():
					r -= 1
			else:
				if s[l].lower() != s[r].lower():
					return False
				else:
					l += 1
					r -= 1
		return True	

    def isPalindrome_two_pointers(self, s):
        start = 0
        end = len(s) - 1 
        status = True
        start_match=None
        end_match=None

        while start < end:
 
        	#For checks in the begining
        	while True:
        		print "start " + str(start)
                	#if start >= end : break
        		if s[start].lower().isalnum():
        			start_match = s[start].lower()
        			start = start + 1
        			break
        		else:
        	            if end - start > 0: start = start + 1
	                    else: return True

			if start >= end : return False  
			if end - start == 2 : return True          


        	while True:
        		print "end "  + str(end)
                	#if start >= end : break
        		if ord(s[end].lower()) > 96 and ord(s[end].lower()) < 123:
        			end_match = s[end].lower()
        			end = end - 1
        			break
        		else:                	    	
				end=end-1

        	print start_match + end_match	
            	#if start_match and end_match: return True

            	#if not start_match or not end_match: return False
        	if start_match != end_match  :
        		status = False
			return status

	return status	


    def isPalindrome(self, s):

	r = ""
	for i in s:
		print ord(i)
        	if (ord(i.lower()) > 96 and ord(i.lower()) < 123) or (ord(i) > 47 and ord(i) < 58) :
					r=r+i
	print r		
	s=r
	if len(s)==0 : return True
	#if len(s)==1 : return False

        start = 0
        end = len(s) - 1 
        status = True
        start_match=None
        end_match=None	
		


        while start < end:
 

            start_match = s[start].lower()
            start = start + 1
            #if start >= end : return False  
            #if end - start == 2 : return True
            end_match = s[end].lower()
            end = end - 1
            print start_match + end_match	
            if start_match != end_match:
                status = False
	return status	



    def isPalindrome_accepted(self, s):

	r = ""
	for i in s:
		print ord(i)
        	if (ord(i.lower()) > 96 and ord(i.lower()) < 123) or (ord(i) > 47 and ord(i) < 58) :
					r=r+i
	
	s=r
	if len(s)==0 : return True
	#if len(s)==1 : return False

        start = 0
        end = len(s) - 1 
        status = True
        start_match=None
        end_match=None	
		
        while start < end:
            start_match = s[start].lower()
            start = start + 1
            #if start >= end : return False  
            #if end - start == 2 : return True
            end_match = s[end].lower()
            end = end - 1
            print start_match + end_match	
            if start_match != end_match:
                status = False
	return status		


    def isPalindrome_to_be_optimized(self, s):

	r = ""
	for i in s:
		print ord(i)
        	if (ord(i.lower()) > 96 and ord(i.lower()) < 123) or (ord(i) > 47 and ord(i) < 58) :
					r=r+i
	
	s=r
	if len(s)==0 : return True
	#if len(s)==1 : return False

        start = 0
        end = len(s) - 1 
        status = True
        start_match=None
        end_match=None	
		
        while start < end:
			
				start_match = s[start].lower()
				start = start + 1
				end_match = s[end].lower()
				end = end - 1
				print start_match + end_match	
				if start_match != end_match:
					status = False

	return status	

		







if __name__ == '__main__':

	a=Solution()
	m=sys.argv[1]
	#m="oABVFDo"
	print a.isPalindrome_suggested(m)





