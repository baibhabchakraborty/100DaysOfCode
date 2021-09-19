#program to find the union and intersection of two sorted arrays

from array import *

arr1 = array('i',[])
arr2 = array('i',[])


print('\nFor first array')
n = int(input('Enter size of array'))
for i in range(n):
    x = int(input('Enter your element'))
    arr1.append(x)


print('\nFor second array')
m = int(input('Enter size of array'))
for i in range(m):
    x = int(input('Enter your element'))
    arr2.append(x)

union = array('i',[])
intersection = array('i',[])

for i in range(n):
    for j in range(m):
        if arr1[i] != arr2[j]:
            union.append(arr1[i])
            union.append(arr2[j])

union_list = union.tolist()                 #convert array to list
union_set = set(union_list)                           

#printing the no of elements directly
print('No of elements in union:',len(union_set))

for i in range(n):
    for j in range(m):
        if arr1[i] == arr2[j]:
            intersection.append(arr1[i])
            intersection.append(arr2[j])

intersection_list = intersection.tolist()                 #convert array to list
intersection_set = set(intersection_list)                           

#printing the no of elements directly
print('No of elements in intersection:',len(intersection_set))