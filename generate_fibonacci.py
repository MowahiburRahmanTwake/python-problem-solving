def generate_fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1

    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b

    return fibonacci_sequence

def main():
    try:
        n = int(input("Enter the length of the Fibonacci sequence: "))
        if n >= 0:
            fibonacci_result = generate_fibonacci(n)
            print(f"The Fibonacci sequence of length {n} is: {fibonacci_result}")
        else:
            print("Please enter a non-negative integer.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
