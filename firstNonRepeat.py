#Find the first non-repeating element in a given array arr of N integers.
#needs revision

from array import *

def nonrepeater(arr,n):
    for i in range(n):
        j = 0
        while(j < n):
            if (i != j and arr[i] == arr[j]):
                break
            j += 1
        if (j == n):
            return arr[i]
      
    return -1


arr = array('i',[])
n = int(input("Enter size of array:"))

for i in range(n):
    x = int(input('Enter array element:'))
    arr.append(x)

#to find first common element

temp = nonrepeater(arr, n)

print('The first non-repeating element in the array is:', temp)