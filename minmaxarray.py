#program to find the minimum element and maximum element of san array

from array import *

arr = array('i',[])


n = int(input("Enter size of array:"))

for i in range(n):
    x = int(input("Enter array element:"))
    arr.append(x)

min = max = arr[0]


for i in range(n):
    if(arr[i] > max):
        max = arr[i]
    
    if(arr[i] < min):
        min = arr[i]

print("Minimum element is ", min)
print("Maximum element is ", max)