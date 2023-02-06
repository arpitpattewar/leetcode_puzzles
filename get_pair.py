


print ("hi")

def get_pair(input, diff):
    dict_result={}
    result=[]
    for i in input:
        a=i-diff
        b=i+diff
        if a in dict_result.values():
            result.append([(i,a)])
        else:
            dict_result[a]=i   
        if b in dict_result.values():
            result.append([(i,b)])
        else:
            dict_result[b]=i  

    print(result)  


if __name__ == '__main__':

    get_pair([1,7,5,9,2,12,3,-1],2)




