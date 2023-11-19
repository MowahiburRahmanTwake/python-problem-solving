# Write a program that determines if a number is positive, negative, or zero.

def check_number_sign(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return ""


num = float(input("Enter a number: "))
result = check_number_sign(num)
print(f"The number {num} is {result}.")
