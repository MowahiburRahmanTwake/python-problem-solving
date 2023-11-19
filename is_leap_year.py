def is_leap_year(year):
    if(year % 4 == 0 & year % 100 != 0 & year % 400):
        return True
    else:
        False

year = int(input("Enter a year: "))

if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")