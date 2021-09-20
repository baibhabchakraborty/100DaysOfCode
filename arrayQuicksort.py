#Program running quicksort
#not getting output

from array import *

def partition(arr,l,h):
    pivot = arr[l]
    i = l
    j = h
    while(i < j):
        while True:
            i += 1
            if(arr[i] <= pivot):
                break
        while True:
            j -= 1
            if(arr[i] > pivot):
                break
        if(i < j):
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    
    return j

def QuickSort(arr,l,h):
    if(l < h):
        j = partition(arr, l, h)
        QuickSort(arr, l, j)
        QuickSort(arr, j+1, h)

n = int(input('Enter size of array:'))
arr = array('i',[])
for i in range(n):
    x = int(input('Enter array element:'))
    arr.append(x)

QuickSort(arr, 0, n-1)

print('The sorted array is:', arr)