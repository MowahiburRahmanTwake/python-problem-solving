# Write a program that determines if a number is even or odd.

# Funcation to determine if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example user
num = int(input("Enter a number: "))
# call funcation
result = check_even_odd(num)

print(f"The number {num} is result {result}")