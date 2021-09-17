#to find peak element where the element is greater than both of it's neighbours

from array import *

arr = array('i',[])                         #array declaration
n = int(input("Enter size of array"))

for i in range(n):                          #array initialization
    x = int(input("Enter element"))
    arr.append(x)

#finding peak element::

for i in range(n):
    if i == 0:
        if arr[0] > arr[1]:
            print(arr[i],"is peak element.")
    elif i == (n-1):
        if arr[i] > arr[i-1]:
            print(arr[i], "is peak element.")
    else:
        if ((arr[i] > arr[i+1]) and (arr[i] > arr[i-1])):
            print(arr[i], "is peak element.")
