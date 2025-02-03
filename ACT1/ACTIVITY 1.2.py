num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 >= num2:
    if num1 >= num3:
        if num2 >= num3:
            descending_order = (num1, num2, num3)  
        else:
            descending_order = (num1, num3, num2)  
    else:
        descending_order = (num3, num1, num2)  
elif num2 >= num3:
    if num1 >= num3:
        descending_order = (num2, num1, num3)  
    else:
        descending_order = (num2, num3, num1)  
else:
    descending_order = (num3, num2, num1)  

print("Numbers in descending order:", descending_order[0], descending_order[1], descending_order[2])