#Given an array a[] of size N which contains elements from 0 to N-1, you need to find all the elements occurring more than once in the given array.

#Example:
#Input:
#N = 4
#a[] = {0,3,1,2}
#Output: -1
#Explanation: N=4 and all elements from 0 to (N-1 = 3) are present in the given array. Therefore output is -1.

from array import *

arr = array('i',[])
n = int(input('Enter length of array:'))
temp = array('i',[])

for i in range(n):
    x = int(input('Enter array element:'))
    arr.append(x)

for i in range(n):
    for j in range(i+1,n):
        if(arr[i] == arr[j]):
            temp.append(arr[i])

l = len(temp)
for i in range(l):
    print(temp[i])
print("are the elements that have duplicates.")