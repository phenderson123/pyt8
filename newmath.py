
num1 = 10
num2 = 14
num3 = 12


num1 = float(input("Enter 1st digit: "))
num2 = float(input("Enter 2nd digit: "))
num3 = float(input("Enter 3rd digit: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The biggest number between",num1,",",num2,"and",num3,"is",largest)