num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 >= num2:
    if num1 >= num3:
        highest = num1
    else:
        highest = num3
elif num2 >= num3:
    highest = num2
else:
    highest = num3

print("The highest number is:", highest)