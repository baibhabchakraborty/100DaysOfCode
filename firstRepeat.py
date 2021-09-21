#Given an array arr[] of size n, find the first repeating element. 
# The element should occurs more than once and the index of its first occurrence 
# should be the smallest.

from array import *

def repeater(arr,n):
    for i in range(n):
        for j in range(i+1,n):
            if(arr[i] == arr[j]):
                temp = arr[i]
                return temp


arr = array('i',[])
n = int(input("Enter size of array:"))

for i in range(n):
    x = int(input('Enter array element:'))
    arr.append(x)

#to find first common element

temp = repeater(arr, n)

print('The first repeating element in the array is:', temp)