#program to move all the negative elements to the end
#uses partition algorithm --> https://www.youtube.com/watch?v=b3z05qLox3w

from array import *

n = int(input('Enter size of array:'))

arr = array('i',[])

for i in range(n):
    x = int(input('Enter array element:'))
    arr.append(x)

#partition algorithm
i = -1
pivot = 0

for j in range(n):
    if arr[j] < pivot:
        i += 1
        arr[i], arr[j] = arr[j], arr[i]

print(arr)