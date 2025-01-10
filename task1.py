# Input number
n = 12345

# Convert the number to a string to easily iterate over each digit
digits = [int(digit) for digit in str(n)]

# Calculate the sum of the digits
sum_of_digits = sum(digits)

# Calculate the average of the digits
average_of_digits = sum_of_digits / len(digits)

# Print the results
print("Sum of digits:", sum_of_digits)
print("Average of digits:", average_of_digits)
