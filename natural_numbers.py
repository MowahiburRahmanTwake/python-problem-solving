# Write a program that prints the first `n` natural numbers.
def print_natural_numbers(n):
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        print(f"The first {n} natural numbers are:")
        for i in range(1, n + 1):
            print(i, end=" ")

def main():
    try:
        n = int(input("Enter the value of n: "))
        print_natural_numbers(n)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()