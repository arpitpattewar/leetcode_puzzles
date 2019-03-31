'''
Created on Mar 24, 2019

@author: aavinash

link: https://leetcode.com/problems/merge-intervals/

'''



#Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        Assuming first element of range is sorted 
        Input: [[1,3],[2,6],[8,10],[15,18]]
        Output: [[1,6],[8,10],[15,18]]
        """
        if intervals:
         if len(intervals) == 1 : return intervals
         else:
            result = [intervals[0]]
            for i in range(1,len(intervals)):
                latest_s,latest_e = result[-1].start, result[-1].end
                ex_s,ex_e = intervals[i].start, intervals[i].end
                
                if ex_s <= latest_e:
                    small = latest_s  if latest_s <= ex_s else ex_s
                    large = latest_e if latest_e >= ex_e else ex_e
                    result.pop()
                    result.append(Interval(s=small, e=large))
                else:
                    #print "yes"
                    result.append(Interval(s=intervals[i].start, e=intervals[i].end))
                        
         return result    
                        
                    
                
                
                
                
            
        
            
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    a=Interval(s=1,e=23)
    b=Interval(s=8,e=28)
    c=Interval(s=-1,e=3)
    d=Interval(s=111,e=223)
    
    f=Interval(s=1,e=4)
    g=Interval(s=4,e=5)
    
    obj = Solution() 
    for i  in obj.merge([f,g]):
        print i.start, i.end
    
    
           