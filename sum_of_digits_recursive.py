def sum_of_digits_recursive(number):
    if number == 0:
        return 0
    else:
        return number % 10 + sum_of_digits_recursive(number // 10)


num = int(input("Enter a number:"))
result = sum_of_digits_recursive(num)
print(f"The sum of digits of {num} is: {result}")
