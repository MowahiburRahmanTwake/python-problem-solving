def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n = int(input("Enter a number: "))
result = fibonacci_recursive(n)
print(f"The {n}th Fibonacci number is: {result}")
