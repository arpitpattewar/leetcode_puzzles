'''
Created on Oct 2, 2018

@author: aavinash
'''

def solution(N):
    # write your code in Python 3.6
    print "1"
    for i in range(2,N+1):
        import functools
        r=[]
        for j in [2,3,5]:
            if i%j == 0 : r.append(j)
        
        if r:
            t=reduce(lambda x,y: x*y,r)
            result = {2:"Codility",3:"Test",5:"Coders",6:"CodilityTest",15:"TestCoders",30:"CodilityTestCoders",10:"CodilityCoders"}
            print result.get(t,i)
        else:
            print i 
            
            
def solution_1(A):
    # write  y our code in Python 3.6

    r1 =  range(1,10)
    r2 = range(-9,0)
    final = list(r1) + list(r2);print (final)
    r= [i for i in A if abs(i)/10 in final ]
    print (r)
    if r:
     return reduce(lambda x,y:x+y,r)
    else : return 0                    
            
 
def solution_3(A):
    # write  y our code in Python 3.6
    import functools
    r1 =  range(1,10)
    r2 = range(-9,0)
    final = list(r1) + list(r2)
    r= [i for i in A if i>0 and len(str(i))==2 in final ]
    r=r+ [i for i in A if i<0 and len(str(i))==3 in final ]
    #print (r)
    if r:
     return functools.reduce(lambda x,y:x+y,r )
    else : return 0  
    
    



if __name__ == '__main__':
    print solution_1([12,-78,200,-11])
    