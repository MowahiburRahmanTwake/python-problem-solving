# Write a program that calculates the volume of a sphere given its radius.
import math


def calculate_sphere_volume(radius):
    volume = (4 / 3) * math.pi * radius ** 3
    return volume


radius = float(input("Enter the radius of the sphere: "))

volume = calculate_sphere_volume(radius)

print(f"The sphere with radious{radius} is: {volume: .2f} cubic units.")
