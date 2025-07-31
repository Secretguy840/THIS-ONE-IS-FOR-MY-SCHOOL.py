import math

print("Shape Calculator")
print("1. Circle")
print("2. Rectangle")
print("3. Square")
print("4. Triangle")

shape = input("Enter shape (1/2/3/4): ")

if shape == '1':
    r = float(input("Enter radius: "))
    print("Area =", math.pi * r**2)
    print("Perimeter =", 2 * math.pi * r)
elif shape == '2':
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    print("Area =", l * w)
    print("Perimeter =", 2 * (l + w))
elif shape == '3':
    s = float(input("Enter side: "))
    print("Area =", s * s)
    print("Perimeter =", 4 * s)
elif shape == '4':
    a = float(input("Enter side 1: "))
    b = float(input("Enter side 2: "))
    c = float(input("Enter side 3: "))
    s = (a + b + c) / 2
    print("Area =", math.sqrt(s * (s-a) * (s-b) * (s-c)))
    print("Perimeter =", a + b + c)
else:
    print("Invalid input")
