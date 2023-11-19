# Write a program that finds the maximum of three numbers.
def find_maximum(num1, num2, num3):
    max_number = max(num1, num2, num3)
    return max_number

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

maximum = find_maximum(num1, num2, num3)

print(f"The maximum of {num1}, {num2}, and {num3}is : {maximum}")