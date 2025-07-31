import math

print("1. Cube")
print("2. Cuboid")
print("3. Sphere")
print("4. Cylinder")

choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
    s = float(input("Enter side: "))
    print("Surface Area =", 6 * s**2)
    print("Volume =", s**3)
elif choice == '2':
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    h = float(input("Enter height: "))
    print("Surface Area =", 2*(l*w + w*h + h*l))
    print("Volume =", l * w * h)
elif choice == '3':
    r = float(input("Enter radius: "))
    print("Surface Area =", 4 * math.pi * r**2)
    print("Volume =", (4/3) * math.pi * r**3)
elif choice == '4':
    r = float(input("Enter radius: "))
    h = float(input("Enter height: "))
    print("Surface Area =", 2 * math.pi * r * (r + h))
    print("Volume =", math.pi * r**2 * h)
else:
    print("Invalid input")
