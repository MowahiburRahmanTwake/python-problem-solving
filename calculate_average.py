# Write a program that finds the average of three numbers.
def calculate_average(num1, num2, num3):
    average = (num1 + num2 +num3)/3
    return average

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

average = calculate_average(num1, num2, num3)

print(f"The avarage number of {num1}, {num2}, and {num3} is = {average:.2f}")
