# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 09:13:58 2019

@author: Gopinath
"""
### create Following [1,2,3,….,19,20]
l1 = range(1,21,1)
l2 = list(l1)
### Reverse Sort [20,19,…,2,1]
##have changeing list3 variable why it changing list2 ?
l3 = l2
l3.reverse() 
print(l3)
### 
l4 = range(1,20)
l5 = list(l4)
l5.reverse()
###[1,2,3,….19,20,19,18,….,2,1]
l6 = l2 + l5
print(l6)

###[4,6,3] and assign it to variable tmp
tmp =[4,6,3]

###[4,6,3,4,6,3,…..,4,6,3] where there are 10 occurences of [4,6,3]
tmp1 = tmp*10
print(tmp1)

###[4,6,3,4,6,3,….,4,6,3,4] where there 10 occurences of [4,6,4] followed by 4
tmp3=[4,6,4]*10
tmp4 = tmp1 + tmp3
tmp4.append(4)
tmp5 = list(tmp4)

'''[4,4,….,4,6,6,….,6,3,3,….,3] where there are 10 occurences of 4, 20 occurences of 6 and 30
occurences of 3'''
t4 = ([4]*10,[6]*20,[3]*30)


'''
Slice the following from list “f”
 0th element
 last but 3 till last element
 downsample by 2 (skip alternative samples)
'''
f=range(0,11)
lis = list(f)
### 0th element
ze = lis[0]
## last but 3 till last element
le = lis[8:] 
# downsample by 2 (skip alternative samples)
ds = range(1,20,2)
rs = list(ds)
