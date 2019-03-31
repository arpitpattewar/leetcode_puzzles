'''
Created on Sep 15, 2018

@author: aavinash
link: https://leetcode.com/problems/combinations/description/
'''



class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        rn = range(1,n+1)
        if k ==1 : return map(lambda x:[x],rn)
        else : 
            if k==n : return [rn]
            #r={}
            s=[]
            for i in self.combine(n, k-1):
                 for j in self.combine(n, 1) :

                     if len(list(set(i).intersection(j))) ==0  :
                         comb = sorted(i+j)
                         v = comb
                         if s.count(v) ==0 : s.append(v)   
            #return r.values()
            return s
        
        

    def combine_1(self, n, k):
        if k == 0:
            return [[]]
        else:
            l=[]
            print k,n
            for i in range(k,n+1) :
                print "i-1={},k-1={}".format(i-1,k-1)
                for pre in self.combine_1(i-1, k-1):
                    print "pre={}".format(pre)
                    l.append(pre + [i])
            return l 
        
        

    def combine_2(self, n, k):
        comb=[[]]
        for i in range(k):  
                 tmp=comb
                 comb=[]
                 for c in tmp :
                     #print "range {}".format(range(1, c[0] if c else n+1))
                     for i in range(1, c[0] if c else n+1):
                         #print "{},c[0]={}".format(tmp, c)
                         comb.append([i]+c );
                     #print comb

        #print r       #comb= [ sorted([v]+k)  for k in comb  for v in range(1,v[0] if v else n+1)  ]            
        return comb


    

if __name__ == '__main__':
    obj = Solution()
    #print obj.combine(13,12)
    #print obj.combine(13,1)
    #print obj.combine(13,10)
    print obj.combine_1(2,1)
