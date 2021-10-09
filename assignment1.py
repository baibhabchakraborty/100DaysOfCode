""" Tax calculator! """


def calculateTax(name, income):
    if income >= 300000:
        tax = 20 * income / 100
    elif income >= 100000:
        tax = 10 * income / 100
    else:
        tax = 0

    
    print(name, ':', tax)



print("Tax Calculator")
print("----------------")

n = int(input("Enter total number count:"))
name = []
income = []

for i in range(n):
    x = input("Enter the name:")
    name.append(x)
    y = int(input("Enter the income:"))
    income.append(y)
    print('\n')

print('Names with liable taxes:')
print('---------------------------')


for j in range(n):
    calculateTax(name[j], income[j])