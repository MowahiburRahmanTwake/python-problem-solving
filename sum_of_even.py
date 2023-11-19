def sum_of_even_numbers(n):

    num_even_numbers = n // 2


    total_sum = num_even_numbers * (num_even_numbers + 1)

    return total_sum

def main():
    try:
        n = int(input("Enter a positive integer to find the sum of even numbers up to it: "))
        if n >= 0:
            result = sum_of_even_numbers(n)
            print(f"The sum of even numbers between 1 and {n} is: {result}")
        else:
            print("Please enter a non-negative integer.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
