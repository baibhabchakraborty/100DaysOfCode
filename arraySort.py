#perform bubble sort in an array


from array import *

arr = array('i',[])
n = int(input("Enter size of array:"))

for i in range(n):
    x = int(input('Enter array element:'))
    arr.append(x)

arr.append(10000000)             #take temporary last element

for i in range(n):
    for j in range(0,n-i):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp


arr.pop(n)                      #delete temporary last element
print('The sorted array is::',arr)


#the above program needs review as it will show an error if one of the elements is > 10000000