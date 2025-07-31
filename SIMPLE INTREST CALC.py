p = float(input("Enter principal amount: "))
r = float(input("Enter interest rate (%): "))
t = float(input("Enter time (years): "))

si = (p * r * t) / 100
total = p + si

print("Simple Interest =", si)
print("Total Amount =", total)
