#this program finds the occurance of an array element(key) in the array, i.e., how many times 
#does that element occur in the array -----> used linear search

from array import *

#array creation
n = int(input('Enter length of array:'))
arr = array('i',[])

for i in range(n):
    x = int(input('Enter array element:'))
    arr.append(x)

k = int(input('Enter your key:'))
c=0

#logic to look for key using linear search
for i in arr:
    if i == k:
        c=c+1

print('The occurance of key is',c)