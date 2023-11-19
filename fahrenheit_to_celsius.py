# Write a program that converts temperature from Fahrenheit to Celsius.
def fahrenheit_to_celsius(fahrenheit):
    celsious = (fahrenheit - 32) * 5 / 9
    return celsious


fahrenheit = float(input("Enter the temperature in Farhrenheit: "))

celsious = fahrenheit_to_celsius(fahrenheit)

print(f"{fahrenheit}degrees Fahrenheit is equal to {celsious:.2f} degrees Celsius.")
