def is_palindrome(input_string):
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
    reversed_string = cleaned_string[::-1]
    return cleaned_string == reversed_string

def main():
    try:
        user_input = input("Enter a string to check if it's a palindrome: ")
        if is_palindrome(user_input):
            print("The entered string is a palindrome.")
        else:
            print("The entered string is not a palindrome.")
    except ValueError:
        print("Invalid input. Please enter a valid string.")

if __name__ == "__main__":
    main()
