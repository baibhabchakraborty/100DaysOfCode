#Program to reverse a string:

str = input('Enter the string you want to reverse:')
strr = []
l = len(str)

#used lists instead of strings since strings are immutable
for i in range(l-1,-1,-1):
    strr.append(str[i]) 
    
strr = ''.join(strr)                        #to convert list to string
print('The reversed string is:',strr)