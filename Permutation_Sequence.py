'''
Created on Aug 26, 2018

@author: aavinash
'''


class Solution(object):
        def getPermutation(self, n, k):
            """
            :type n: int
            :type k: int
            :rtype: str
            """
            numstring = "123456789"
            #return self.display_combination(numstring[:n])[k]
            #return sorted([i for i in self.display_combination_1(numstring[:n])])[k]
            return sorted(  [i for i in self.display_combination_1(numstring[:n])]  )[k] if n !=1 else "1"
    
                
                
        def display_combination(self, input):
            if len(input) == 1: return [input]
            if len(input) == 2: return  [input,input[::-1]]
            else:    
                result = []
                for i in range(len(input)):
                    for j in self.display_combination(input[0:i]+input[i+1:len(input)]):
                        result.append(input[i]+j)
            return result
        
        
        
        
        def display_combination_1(self, elements):
            if len(elements) <=1:
                yield elements
            else:
                for perm in self.display_combination_1(elements[1:]):
                    for i in range(len(elements)):
                        # nb elements[0:1] works in both string and list contexts
                        yield perm[:i] + elements[0:1] + perm[i:]
                
                    
                
        
        
        
        

if __name__ == '__main__':
    obj = Solution()
    print obj.getPermutation(9,171669)
    #print obj.display_combination("1234")
    