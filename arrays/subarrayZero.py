"""Given an array of positive and negative numbers. Find if there is a subarray (of size at-least one) with 0 sum.

Example 1:

Input:
5
4 2 -3 1 6

Output: 
Yes

Explanation: 
2, -3, 1 is the subarray 
with sum 0."""

#needs review

from array import *

n = int(input('Enter length of array:'))

arr = array('i',[])

for i in range(n):
    x = int(input('Enter array element:'))
    arr.append(x)

c = 0

for i in range(n):
    cur_sum = arr[i]
    j = i + 1

    while j <= n:
        if cur_sum == 0:
            print("Subarray found between")
            print("indexes % d and % d" %( i, j-1))
            c = 1
        if ((cur_sum > 0) or (j == n)):
            break

        cur_sum = cur_sum + arr[j]
        j += 1

if(c != 1):
    print('No subarray found')