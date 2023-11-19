
# Write a program that swaps the values of two variables.

def swap_variable(var1, var2):
    temp = var1
    var1 = var2
    return var1, var2


a = int(input("var1: "))
b = int(input("var2: "))

print(f"Before swapping: a = {a}, b = {b}")

# Call swap function
a, b = swap_variable(a, b)
print(f"After swapping: a = {a}, b = {b}")
