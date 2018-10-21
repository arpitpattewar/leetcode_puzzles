'''
Created on Jul 21, 2018

@author: aavinash
'''



def binary_search(input, num):
    if input[-1] >= num:

            middle_number=input[len(input)/2]
    
            if middle_number > num:
                binary_search(input[:len(input)/2], num)
            
            elif middle_number < num:
                binary_search(input[len(input)/2:], num)
            else:
                return True  
    else:
        return False    
    
    
def searchRange(input,num): 
   llen=len(input)
   if len(input) == 1:
        if input[0] == num : return [0,0]
        else: return [-1,-1]
   else: 
    middle_index = llen/2
    start = 0
    end = llen
    leftside = None
    while end-start >= 1:
        #print start,end
        if num > input[middle_index]:
            start = middle_index
            end = end
        elif num < input[middle_index]:   
            start =start
            end =  middle_index
        else:            
            leftside = middle_index-1
            rightside = middle_index+1
            
            while leftside >=0 and input[leftside] == num:
                leftside-=1
                
            while rightside < llen and input[rightside] == num:
                rightside+=1        
            break    
        middle_index = start + (end - start)/2  
    if  leftside is  None : return [-1,-1]
    elif  leftside+1 ==  rightside-1 :    return [middle_index,middle_index]
    else: return [leftside+1,rightside-1]
        
        
    
     
            
        
    
    

if __name__ == '__main__':
    s=range(10)+[81,100,130,155,169,786,900,1323]
    s=[1,2,3,4,5,6,7,7,7,7,7,7,7,7,7,7,7,7,8,9,11,23]
    s=[2,2]
    s=[2,3]
    s=[5,7,7,7,7,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,10]
    #s=[1,56]
    
    print searchRange(s,8)
    