def reverse_number(number):
    reversed_num = 0

    while number > 0:
        digit = number % 10
        reversed_num = reversed_num * 10 + digit
        number //= 10

    return reversed_num

def main():
    try:
        num = int(input("Enter a number to reverse: "))
        reversed_result = reverse_number(num)
        print(f"The reversed number is: {reversed_result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
