# Multiple functions
import math

def circle_area(radius):
    return math.pi * radius * radius

def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height

print("Area Calculator")
print("===============")

print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = input("Choose shape (1-3): ")

if choice == '1':
    r = float(input("Enter radius: "))
    print(f"Area of circle = {circle_area(r):.2f}")
elif choice == '2':
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    print(f"Area of rectangle = {rectangle_area(l, w)}")
elif choice == '3':
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    print(f"Area of triangle = {triangle_area(b, h)}")
else:
    print("Invalid choice!")
