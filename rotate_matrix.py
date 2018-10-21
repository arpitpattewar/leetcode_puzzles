'''
Created on Aug 7, 2018

@author: aavinash
'''



def rotateMatrix(mat):
 
    if not len(mat):
        return
     
    """
        top : starting row index
        bottom : ending row index
        left : starting column index
        right : ending column index
    """
 
    top = 0
    bottom = len(mat)-1
 
    left = 0
    right = len(mat[0])-1
 
    while left < right and top < bottom:
 
        # Store the first element of next row,
        # this element will replace first element of
        # current row
        prev = mat[top+1][left]
 
        # Move elements of top row one step right
        for i in range(left, right+1):
            curr = mat[top][i]
            mat[top][i] = prev
            prev = curr
        print "first {}".format(mat)    
 
        top += 1
 
        # Move elements of rightmost column one step downwards
        for i in range(top, bottom+1):
            curr = mat[i][right]
            mat[i][right] = prev
            prev = curr
        print "second {}".format(mat)     
 
        right -= 1
 
        # Move elements of bottom row one step left
        for i in range(right, left-1, -1):
            curr = mat[bottom][i]
            mat[bottom][i] = prev
            prev = curr
 
        bottom -= 1
 
        # Move elements of leftmost column one step upwards
        for i in range(bottom, top-1, -1):
            curr = mat[i][left]
            mat[i][left] = prev
            prev = curr
 
        left += 1
 
    return mat

if __name__ == '__main__':
    
    matrix =[ 
            [1,  2,  3,  4 ],
            [5,  6,  7,  8 ],
            [9,  10, 11, 12 ],
            [13, 14, 15, 16 ]  
        ]
    print "Actual {}".format(matrix)
    print rotateMatrix(matrix)
    