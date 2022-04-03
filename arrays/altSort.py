""" Alternate positive and negative numbers 
Easy Accuracy: 49.41% Submissions: 27183 Points: 2
Given an unsorted array Arr of N positive and negative numbers. Your task is to create an array of alternate positive and negative numbers without changing the relative order of positive and negative numbers.
Note: Array should start with positive number.
 

Example 1:

Input: 
N = 9
Arr[] = {9, 4, -2, -1, 5, 0, -5, -3, 2}
Output:
9 -2 4 -1 5 -5 0 -3 2
"""


from array import *
import numpy as np

arr = array('i',[])
n = int(input("Enter size of array:"))

for i in range(n):
    x = int(input('Enter array element:'))
    arr.append(x)

pos = []
neg = []

for i in range(n):
    if(arr[i] < 0):
        neg.append(arr[i])
    elif(arr[i] == 0):
        pos.append(arr[i])
    else:
        pos.append(arr[i])

pos.sort()
neg.sort()
print(pos)
print(neg)

final = []
p = 0
ne = 0

for j in range(n):
    if(j % 2 == 0):
        final.append(pos[p])
        p = p + 1
        
    else:
        final.append(neg[ne])
        n = n + 1
        

#print(final)
arr = np.array(final)

print(arr)
