# Loop with accumulator
print("Sum of Natural Numbers")
print("=====================")

n = int(input("Enter a number: "))
sum_natural = 0

for i in range(1, n + 1):
    sum_natural += i

print(f"Sum of first {n} natural numbers = {sum_natural}")
