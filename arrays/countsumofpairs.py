#Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.

#Example:
#Input:
#N = 4, K = 6
#arr[] = {1, 5, 7, 1}
#Output: 2
#Explanation: 
#arr[0] + arr[1] = 1 + 5 = 6 and arr[1] + arr[3] = 5 + 1 = 6.
#https://www.youtube.com/watch?v=bvKMZXc0jQU

from array import *

arr = array('i',[])
n = int(input('Enter size of array:'))

for i in range(n):
    x = int(input('Enter array element:'))
    arr.append(x)

sum = int(input('Enter the sum:'))
count = 0

for i in range(n):
    for j in range(i+1,n):
        if(arr[i]+arr[j] == sum):
            count+=1

print(count)