"""
Given an array Arr[] that contains N integers (may be positive, negative or zero). Find the product of the maximum product subarray.

Example 1:

Input:
N = 5
Arr[] = {6, -3, -10, 0, 2}
Output: 180
Explanation: Subarray with maximum product
is [6, -3, -10] which gives product as 180.
"""
"""
from array import *

def prodSubarray(arr, n):
    maxvalue = 0
    for i in range(n):
        for j in range(i, n):
            temp = 1
            for k in range(i, j+1):
                temp = temp * arr[k]

                if temp > maxvalue:
                    maxvalue = temp

    return maxvalue



arr = array('i',[])                         #array declaration
l = int(input("Enter size of array"))

for i in range(l):                          #array initialization
    x = int(input("Enter element"))
    arr.append(x)

if l == 0:
    print(int(-1))
else:
    maxelement = prodSubarray(arr,l)
    print(maxelement)
"""

#this above program doesnt work for one array element properly
#time = o(n^2)

from array import *

def prodSubarray(arr, n):
    minProd = maxProd = ans = arr[0]
    for i in range(1,n):
        choice1 = minProd * arr[i]
        choice2 = maxProd * arr[i]

        minProd = min(a[i], min(choice1, choice2)) 
        maxProd = max(a[i], max(choice1, choice2))
        ans = max(ans, maxProd)

    return ans   



arr = array('i',[])                         #array declaration
l = int(input("Enter size of array"))

for i in range(l):                          #array initialization
    x = int(input("Enter element"))
    arr.append(x)

if l == 0:
    print(int(-1))
else:
    ans = prodSubarray(arr,l)
    print(ans)