"""first_item = lambda my_list : my_list[0]
first_item = (['cat','dog','elephant'])
print(first_item)"""

import math
num = [-3,-5,1,4]
l = list(map(lambda x : 1/ (1 + math.exp(-x)),num))
print(l)

names = ['karen','jim','kim']
k = list(filter(lambda name : len(name)== 3,names))
print(k)