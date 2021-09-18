#this program sorts an array of only 0s, 1s, and 2s

from array import * 
import numpy as np

#array creation
n = int(input('Enter length of array:'))
arr = array('i',[])

for i in range(n):
    x = int(input('Enter array element of 0, 1, 2:'))
    arr.append(x)

arr_list = arr.tolist()                 #convert array to list
arr_list.sort()                         #sort array
arr = np.array(arr_list)                #convert list to array

print('The sorted array is:',arr)