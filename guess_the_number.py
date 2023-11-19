import random

def guess_the_number():
    lower_limit = 1
    upper_limit = 100
    target_number = random.randint(lower_limit, upper_limit)

    print(f"Guess the number between {lower_limit} and {upper_limit}")

    attempts = 0
    while True:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess == target_number:
            print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")
            break
        elif user_guess < target_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

def main():
    print("Welcome to the Guess the Number Game!")
    guess_the_number()

if __name__ == "__main__":
    main()
