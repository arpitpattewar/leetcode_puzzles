


def findTwo(input, target):
	start = 0
	end = len(input) - 1 
	result=[]
	input = sorted(input)
	while start < end:
		ssum = input[start] +input[end]
		if  ssum <= target:
			if ssum == target: result.append((input[start],input[end]))
			start = start + 1
		else:
			end = end - 1
	return result


def toString(List): 
    return ''.join(List) 



def permute(a, l, r): 
    if l == r: 
        print(toString(a)) 
    else: 
        for i in range(l, r): 
			print ("Swapping i={},l={}, a[l]={} , a[i]={} ".format(i,l,a[l], a[i]))
			a[l], a[i] = a[i], a[l] 
			print ("Calling permute again with a={},l+1 ={} and r={}".format(a, l+1, r ))
			permute(a, l+1, r) 
			a[l], a[i] = a[i], a[l] 


if __name__ == '__main__':	
	print(permute(["A","B","C"],0,3))




