def sum_digits(input_string):
    digit_sum = 0

    for char in input_string:
        if char.isdigit():
            digit_sum += int(char)

    print("Sum of digits:", digit_sum)

input_string = input("Enter a string with digits: ")
sum_digits(input_string)
