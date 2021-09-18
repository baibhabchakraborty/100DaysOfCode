#this program gives us the kth maximum and kth minimum element in an array

from array import *
import numpy as np

#creation of the array
arr = array('i',[])
n = int(input('Enter array length:'))

for i in range(n):
    x = int(input('Enter the element:'))
    arr.append(x)

k = int(input('Enter value of K:'))



arr_list = arr.tolist()                     #convert array to list
arr_list.sort()                             #sort the list
arr = np.array(arr_list)                    #convert list back to array

print('The kth min element is:',arr[k-1])
print('The kth max element is:',arr[n-k])
