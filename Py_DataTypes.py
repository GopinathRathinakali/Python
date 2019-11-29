# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 17:49:43 2019

@author: GR
"""
############# Datatypes ###################################
#Python has the following data types built-in by default, in these categories:
#Text Type:	str
#Numeric Types:	int, float, complex
#Sequence Types:	list, tuple, range
#Mapping Type:	dict
#Set Types:	set, frozenset
#Boolean Type:	bool
#Binary Types:	bytes, bytearray, memoryview

TNS SMS BB
################### String #####################################
str = "Hello Python World"
print(str)
type(str) #Type() help to getto know the which type of datatype 

"""Output for string
Hello Python World
Out[15]: str
"""

############# Numeric Types ###################################
x_int = 10
x_float = 10.5
x_complex = 10j

print(x_int,x_float,x_complex)
print(type(x_int),type(x_float),type(x_complex))
""" Output for numeric
10 10.5 10j
<class 'int'> <class 'float'> <class 'complex'>

"""

############# Sequence Types ###################################
x_list = [3,5,6,2,1,8,9]
x_tuple = (9,7,5,3,2,1)
print(x_list)
type(x_list),type(x_tuple)
x_range = range(5)
x_lst = list(x_range)
print(x_lst)
""" 
OUTPUT for List 
[3, 5, 6, 2, 1, 8, 9]
Out[13]: list

Output for tuple
(9, 7, 5, 3, 2, 1)
Out[16]: tuple

Output for range
[0, 1, 2, 3, 4]
"""

##################Mapping Type################################
##list uses []
##tuple uses ()
##dictionary & set uses {}

x_dict =  { "emp1": 'xyz',
             "emp2": 'ABC',
             "emp3":'IJK'              
           }

print(x_dict)

####################Set Types:	set, frozenset######################
x_set  = {4,5,8,5,2,64,3,3,3,3,3,78,5,4}
print(x_set)
x_frozenset = {4,5,6,3}
#print(x_frozenset)

x_frozenset ={5,6,3,5,2,3,0}
print(x_frozenset)


###################Boolean Type:	bool############################
x_bool_T = True + False + True
print(x_bool_T)

x_bytes = bytes(5)		
x_bytarray = bytearray(5)
x_mv = memoryview(bytes(5))
print(x_bytes,x_bytarray,x_mv)

