#program to find sub array that add up to a given sum within an array

#needs revision - https://www.youtube.com/watch?v=Ofl4KgFhLsM

from array import *

n = int(input('Enter length of array:'))

arr = array('i',[])

for i in range(n):
    x = int(input('Enter array element:'))
    arr.append(x)

sum = int(input('Enter the sum:'))
c=0

for i in range(n):
    cur_sum = arr[i]
    j = i + 1

    while j <= n:
        if cur_sum == sum:
            print("Sum found between")
            print("indexes % d and % d" %( i, j-1))
            c=1
        if cur_sum > sum or j == n:
            break

        cur_sum = cur_sum + arr[j]
        j += 1

if(c != 1):
    print('No subarray found')