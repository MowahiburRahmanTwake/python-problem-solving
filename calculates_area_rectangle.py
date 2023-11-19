def calculate_rectangle_area(length, width):
    area = length * width
    return area


# input user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# call calculate rectangle area

area = calculate_rectangle_area(length, width)
print(f"calculate rectangle length {length} and width {width} is: {area}")
