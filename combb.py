'''
Created on Feb 7, 2019

@author: aavinash
'''

def combb(input):
  lth =  len(input)
  if lth ==2 : 
      #yield input[::-1]
      yield input
  if lth ==1: yield input
  else:
      #r=[]
      big = input[:lth-1]
      small = input[lth-1:]
      big_list = combb(big)
      small_list=combb(small)
      for i in big_list:
          for j in range(len(i)+1):
              yield i[:j] +[small]+ i[j:]
      #yield r               


if __name__ == '__main__':
    print [i for i in combb([1,2])]