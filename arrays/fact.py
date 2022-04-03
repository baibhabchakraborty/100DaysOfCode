""" 
To find the factorial of a large number
Input: N = 5
Output: 120
Explanation : 5! = 1*2*3*4*5 = 120
"""

n = int(input("Enter number:"))
temp = n
fact = 1

while temp != 0:
    fact = fact * temp
    temp = temp -1

print(fact)