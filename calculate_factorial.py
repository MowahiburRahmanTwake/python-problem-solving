# Write a program that calculates the factorial of a number.
def calculate_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def main():
    try:
        num = int(input("Enter a non-negative integer to calculate its factorial: "))
        if num >= 0:
            factorial_result = calculate_factorial(num)
            print(f"The factorial of {num} is: {factorial_result}")
        else:
            print("Please enter a non-negative integer.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
