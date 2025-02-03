first_term = int(input("Enter first term number: "))
last_term = int(input("Enter last term number: "))

sum_of_numbers = 0

for num in range(first_term, last_term + 1):
    sum_of_numbers += num

print("The sum of the numbers from", first_term, "to", last_term, "is", sum_of_numbers)