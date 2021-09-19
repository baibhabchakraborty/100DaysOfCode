#Given an array, rotate the array by one position in clock-wise direction.
 
#Example:
#Input:
#N = 5
#A[] = {1, 2, 3, 4, 5}
#Output: 5 1 2 3 4
 
from array import *

arr = array('i',[])
n = int(input('Enter size of array:'))

for i in range(n):
    x = int(input('Enter array element:'))
    arr.append(x)

arr.append(1000000)                             #take a temp element

for i in range(n-1,-1,-1):
    #print(i)
    arr[i+1] = arr[i]

arr[0] = arr[n]
arr.pop()
print(arr)