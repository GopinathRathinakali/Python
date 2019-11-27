## ()
  # Passing inputs to a function
  # Creating tuples

## []
  # Creating list
  # Slicing
## {}
  # Creating dictionary as {key:value} pair format
  # Creating set by giving values within {}

############# Atomic Datatypes ###################################
# int, float, string,bool, complex

################### integer #####################################
# any number without decimal space is assigned as integer
a = 2
type(a)
b = -10
c = 11314757684568456847854684787845784874587648
#c1 = 05 # throws error as it is not a valid number


################# float ############################
# any number with decimal point
d = 5.6
type(d)
d1 = 6.0
# int to float
b2 = float(b)
# float to int
d2 = int(5.6) # floor to the smalles integer
d3 = round(5.6)
d4 = round(5.4)

#################### String ############################
# anything given within quotes is a string
s = "nature"
type(s)
s2 = 'water'
s3 = "999"
s + s2 # + of 2 strings is concatenation
s2 + s3
#s3 + 5# throws error

# string to numbers
s3i = int(s3)
s3i + 5
#int(s) # throws error
di = int("05") # removes leading zeros

## User inputs will be read as string
ip1 = input("Enter input 1: ")
ip2 = input("Enter input 2: ")
print(ip1+ip2)

ip1 = input("Enter input number 1: ")
ip2 = input("Enter input number 2: ")
print(int(ip1) + int(ip2))

################ Boolean ######################################
# True, False

f = True
type(f)
g = False
type(g)
#h = false # python is case sensitive
G = True
f1 = 5 > 6
f2 = 6 > 5
f3 = 5 == 6 # equality check ==
f4 = 5 == 5
f5 = 5 != 6
f1 and f2
f1 or f2
not(f1)

# + of booleans will return count of Trues
True + False + True
False + True + False + False
False + False + False

################# Complex ##############################
# Real and imaginary part
h = 5 + 10j
type(h)
h.real
h.imag
# (a + bj)*(a - bj) = a^2 - abj + abj- b^2j^2 = a^2 + b^2
m = 5 - 10j
h*m

################## tuple ################################
# set of values within paranthesis

t1 = (1,2,5,8,4,6)
type(t1)
t2 = 1,2,5,8,4,3 # this is also a tuple. But NOT recommended without ()
len(t1) # number of elements in a tuple
t1 + t2
t3 = ("nature","water","forest")
t4 = (1, 5.6, True, "nature", 6 + 10j) # you can have mix of data types

## TUPLE SLICING
t1[0]
t1[3]
t1[len(t1) - 1] # last element
t1[len(t1) - 2] # last but one element
t1[-1]
t1[-2]
t1[-3]
#t1[2] = 99 # throws error
# Tuples are immutable (they cannot be edited)

################33 List #############################
# one of the most popular data type
# Values given within square brackets
l1 = [1,4,7,4,3,9]
type(l1)
l3 = list(t3) # converting tuple to a list
l4 = [1,5.6,True,"nature"] # mix of data types is possible in liat as well
l1[3] = 99 # lists are mutable

## LIST OPERATIONS
l1.append(100)
l1.append(7)
l1.insert(4,88) # insert value in a position
l1.extend(l4) # extending values of one list with another
l5 = l1 + l3 # concatenation of 2 lists
l5.count(7)
l1.index(4) # index correspoonding to a value
l1.index(88)
l1.index(7) # returns the first occurence
l1.remove(88) # removes a value
l1.remove(7) # removes only the first occurence
del l1[3] # removes value in a position

l6 = [1,8,7,5,3,6]
l6.reverse()
l6.sort()
l6.sort(reverse = True) # descending order

# Q: How to create a new list after list operation
# Ans: Make a copy
l7 =[1,8,7,5,3,6]
l8 = l7.copy() # to copy a variable
l8.reverse()

l9 = l7 # this is NOT a copy. both variables are pointing to same memory location
l9[2] = 100

l7 = ["nature","flood","Water","Ocean"]
l7.sort(key = str.lower)
h = l6.sort() # sort doesn't return any output
print(h) # None

#### Sequence of numbers
lseq = [1,2,3,4,5,6,7,8,9,10]

rr = range(1,10,1)
type(rr)
lseq2 = list(range(1,10,1)) # 1,2,3,....,9
lseq3 = list(range(1,11,1)) # 1,2,3,.....,10
lodd = list(range(1,11,2)) #1,3,5,7,9

list(range(5)) # taken as stop. default start is 0
list(range(1,6)) # default step size will be 1

sum(lseq)

### Repeat values
lrep1 = [5]*10
lrep2 = [1,2,3]*10

## LIST SLICING
l5[0]
l5[-1]
l5[1:5] # 1st till 4th position
l5[:5] # first 5 elements
l5[-5:] # last 5 elements
l5[1:10:2] # skips alternative samples
l5[1:10:3] 

## LIST SEARCHING
99 in l5
77 in l5
77 not in l5

## LIST OF LIST
l10 = [1,2,3]
l11 = [5,6,7]
l12 = [l10,l11]

l12[0][1]
l12[1][2]

#### Additional references
#### List assignment
#Create following lists
#a) [1,2,3,….,19,20]
a = list(range(1,21))

#b) [20,19,…,2,1]
b = a.copy()
b.reverse() # option 1
b = list(range(20,0,-1)) # option 2

#c) [1,2,3,….19,20,19,18,….,2,1]
c = a + b
c.remove(20) # option 1
c = a + b[1:] # option 2

#d) [4,6,3] and assign it to variable tmp
tmp = [4,6,3]

#e) [4,6,3,4,6,3,…..,4,6,3] where there are 10 occurences of [4,6,3]
e = tmp*10

#f) [4,6,3,4,6,3,….,4,6,3,4] where there 10 occurences of [4,6,3] followed by 4
f = e.copy()
f.append(4) # option 1
f = e + [4] # option 2

#g) [4,4,….,4,6,6,….,6,3,3,….,3] where there are 10 occurences of 4, 
# 20 occurences of 6 and 30 occurences of 3
g = [4]*10 + [6]*20 + [3]*30

#Slice the following from list “f”
# 0th element
f[0]
# last but 3 till last element
f[-4:]

# downsample by 2 (skip alternative samples)
f3 = f[::2]

#################### dictionary ####################
# save data in a {Key:Value} pair format

math_score_list = [95,67,88,45,84]
math_score_list[0]
math_score_list[3]

math_score_dict = {"R101": 95,
                   "R108": 67,
                   "R102": 88,
                   "R109": 45,
                   "R105": 84}
type(math_score_dict)
math_score_dict["R108"]
#math_score_dict[3] # dictionary cannot be sliced using position
# Position doesn't matter in case of dictionary

## Keys have to be unique. Duplicate will replace original
math_score_dict2 = {"R101": 95,
                   "R108": 67,
                   "R102": 88,
                   "R108": 45,
                   "R105": 84}

math_score_dict.keys()
math_score_dict.values()

math_score_dict["R100"] = 99 # insert a new key value pair

## Keys of dictionary should be of immutable data type
## Values can be of any data type
somedict = {1: "hello",
            (6,"Water"): [6,5,2,3],
            "Nat": {"A": 5.6, "B":6.7}}
"""
below will throw error as list is not permissible as key
somedict2 = {1: "hello",
            [6,"Water"]: [6,5,2,3],
            "Nat": {"A": 5.6, "B":6.7}}
"""
########### Practice 
# Create the following 2 dictionaries
states = {
    'Oregon':'OR',
    'Florida':'FL',
    'California':'CA',
    'New York': 'NY',
    'Michigan':'MI'}

cities = {
    'CA':'San Fransico',
    'MI': 'Detroit',
    'NY':'Manhattan'}
# what is the name of the city in state "MI"
# Add a city 'Orlando' to 'FL'
# what is the city name in 'New York' State

####################### set #####################################
s1 = {1,5,4,3,7,8,4,6,7,3,5,7,8,8,6,4,3,5,6,7}
type(s1)
print(s1) # set will have only unique values

# set can be used as a work-around to remove duplicates

setA = {1,2,3,4,5}
setB = {4,5,6,7,8}
setA & setB # Intersection
setA | setB # Union (pipe)
setA - setB # values in A which are NOT present in B

lA = list(setA) # set can be converted to a list and vice versa

################ Datetime #####################################
import datetime # pre-installed with python

## Date
dd = datetime.date(2019,11,24)
print(dd)
dd.day
dd.month
dd.weekday() # Monday starts with 0
dtod = datetime.date.today()
print(dtod)
dtod.weekday()


## Datetime
dtnow = datetime.datetime.now()
print(dtnow)
dtnow.month
dtnow.weekday()
dtnow.hour
dtnow.minute

# Reference
#https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

#### STRPTIME: Custom format to standard format
dd1 = datetime.datetime.strptime("25/11/2019","%d/%m/%Y")
dd1.month
dd2 = datetime.datetime.strptime("25-11-2019","%d-%m-%Y")
dd3 = datetime.datetime.strptime("Nov 25, 2019","%b %d, %Y" )

### STRFTIME: Standard format to custom format
ds1 = datetime.datetime.strftime(dtod,"%d-%m-%Y")
ds2 = datetime.datetime.strftime(dtod,"%b %d, %Y")

###################################################################

math_score_list = [95,67,88,45,84]
min(math_score_list)
max(math_score_list)

avg_maths = sum(math_score_list)/len(math_score_list) # average
var_maths = (95 - 75.8)**2 + (67 - 75.8)**2 + (88 - 75.8)**2 + (45 - 75.8)**2 + (84 - 75.8)**2 # variance
std_maths = var_maths**0.5 # standard deviation

## Median
math_score_list2 = math_score_list.copy()
math_score_list2.sort()
math_score_list2[int(len(math_score_list2)/2)]

math_score_list3 = [95,67,88,45,84,62] # length is even
math_score_list4 = math_score_list3.copy()
math_score_list4.sort()

(math_score_list4[int(len(math_score_list2)/2)] + 
math_score_list4[int(len(math_score_list2)/2) + 1])/2

################### numpy ############################################
import numpy as np # preinstalled with anaconda

np.mean(math_score_list)
np.median(math_score_list)
np.std(math_score_list)

## numpy array
## vectorized operation
## numpy matrix
math_score_list = [95,67,88,45,84,62]
npary = np.array(math_score_list)
type(npary)

arr1 = np.arange(1,10,2)
arr2 = np.random.seed(352)
arr2 = np.random.randint(1,10,3)
arr2

math_score_array = np.array(math_score_list.copy())
math_score_array = math_score_array + 1
math_score_array1 = math_score_array >80

arr3 = np.array([3,4,5,6])
arr4 = np.array([True,False,True,True])

arr5 = np.random.randint(1,100,10)
arr5

rsh = np.reshape(arr5,[2,5])
rsh