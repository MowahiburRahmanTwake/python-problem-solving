# Write a program that prints the multiplication table of a given number.
def print_multiplication_table(number, limit=10):
    print(f"Multiplication table for {number} up to {limit}:")

    for i in range(1, limit + 1):
        result = number * i
        print(f"{number} x {i} = {result}")

def main():
    try:
        num = int(input("Enter a number to print its multiplication table: "))
        limit = int(input("Enter the limit (default is 10): ") or "10")

        if num > 0:
            print_multiplication_table(num, limit)
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main()
