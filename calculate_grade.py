# Write a program that calculates the grade based on a given percentage.
def calculate_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'
def main():
    try:
        percentage = float(input("Enter the percentage: "))
        if 0 <= percentage <= 100:
            grade = calculate_grade(percentage)
            print(f"The grade for {percentage}% is: {grade}")
        else:
            print("Percentage must be between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()