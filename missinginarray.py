#Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.
#solution --> https://www.youtube.com/watch?v=6KHW7ZQwtCA   (not reqd)

#Example:
#Input:
#N = 5   then array elements = {1-5}
#A[] = {1,2,3,5}
#Output: 4

from array import *

n = int(input('Enter size of array:'))
arr = array('i',[])

for i in range(n-1):
    x = int(input('Enter array element:'))
    arr.append(x)

sum = n * (n + 1) / 2           #sum of n natural numbers

count = 0

for i in range(n-1):
    count = count + arr[i]

if(count > n):
    print('The missing number is:', int(sum-count))
else:
    print('There are 2 or more numbers missing! Please recheck')